import os
import json
import shutil
import hashlib
from datetime import datetime

SNAPSHOT_DIR = "snapshots"
META_FILE = os.path.join(SNAPSHOT_DIR, "history.json")


def ensure_setup():
    if not os.path.exists(SNAPSHOT_DIR):
        os.mkdir(SNAPSHOT_DIR)
    if not os.path.exists(META_FILE):
        with open(META_FILE, "w") as f:
            json.dump([], f)


def file_hash(filepath):
    with open(filepath, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def save_snapshot(filepath):
    ensure_setup()

    if not os.path.exists(filepath):
        print("❌ File does not exist")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.basename(filepath)
    snapshot_name = f"{filename}_{timestamp}"

    shutil.copy(filepath, os.path.join(SNAPSHOT_DIR, snapshot_name))

    with open(META_FILE, "r") as f:
        history = json.load(f)

    history.append({
        "snapshot": snapshot_name,
        "time": timestamp,
        "hash": file_hash(filepath)
    })

    with open(META_FILE, "w") as f:
        json.dump(history, f, indent=2)

    print("✅ Snapshot saved:", snapshot_name)


def show_history():
    ensure_setup()

    with open(META_FILE, "r") as f:
        history = json.load(f)

    if not history:
        print("No history found")
        return

    for i, h in enumerate(history):
        print(f"{i} → {h['snapshot']}  ({h['time']})")


def restore_snapshot(index, target_file):
    ensure_setup()

    with open(META_FILE, "r") as f:
        history = json.load(f)

    if index < 0 or index >= len(history):
        print("❌ Invalid snapshot index")
        return

    snapshot_file = os.path.join(SNAPSHOT_DIR, history[index]["snapshot"])
    shutil.copy(snapshot_file, target_file)

    print("🔁 File restored successfully")


# -------- CLI --------
if __name__ == "__main__":
    print("""
Local Code Time Machine
1. Save snapshot
2. Show history
3. Restore snapshot
""")

    choice = input("Choose option: ")

    if choice == "1":
        file = input("Enter file path: ")
        save_snapshot(file)

    elif choice == "2":
        show_history()

    elif choice == "3":
        idx = int(input("Enter snapshot index: "))
        file = input("Enter target file path: ")
        restore_snapshot(idx, file)

    else:
        print("Invalid choice")
