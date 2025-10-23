
# filepath: [preprocessor.py](http://_vscodecontentref_/5)
# ...existing code...
import re
import pandas as pd

def preprocess(text: str) -> pd.DataFrame:
    """
    Parse WhatsApp exported chat text and return a DataFrame with:
    - date (datetime), user (str), message (str), year, month, day, hour
    """
    # Regex to detect message start lines (common formats; may need tweak for your locale)
    dt_re = re.compile(r'^(\d{1,2}/\d{1,2}/\d{2,4}),?\s+(\d{1,2}:\d{2}(?:\s?[APMapm]{2})?)\s+-\s+')
    entries = []
    current = None

    for line in text.splitlines():
        m = dt_re.match(line)
        if m:
            # start of a new message
            if current:
                entries.append(current)
            date_str = f"{m.group(1)} {m.group(2)}"
            content = line[m.end():].strip()
            current = {"date_str": date_str, "raw": content}
        else:
            # continuation of previous message
            if current:
                current["raw"] += "\n" + line
            else:
                # skip garbage before first message
                continue

    if current:
        entries.append(current)

    if not entries:
        return pd.DataFrame(columns=["date", "user", "message"])

    df = pd.DataFrame(entries)
    # parse dates (coerce errors if format differs)
    df["date"] = pd.to_datetime(df["date_str"], errors="coerce")
    # split user and message; system messages may not have ': '
    def split_user(msg):
        parts = msg.split(": ", 1)
        if len(parts) == 2:
            return parts[0], parts[1]
        return ("system", msg)

    df[["user", "message"]] = df["raw"].apply(lambda s: pd.Series(split_user(s)))
    df['only_date'] = df['date'].dt.date
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month_name()
    df["day"] = df["date"].dt.day
    df["day_name"] = df["date"].dt.day_name() 
    df["hour"] = df["date"].dt.hour
    df['month_num'] = df['date'].dt.month

    # drop intermediates
    df = df[["date","only_date", "user", "message", "year", "month","month_num", "day", "day_name", "hour"]]
    return df
# ...existing code...