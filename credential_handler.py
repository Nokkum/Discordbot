import tkinter as tk
from tkinter import messagebox, ttk
import subprocess
import os
from cryptography.fernet import Fernet

BASE_DIR = os.path.join(os.getcwd(), ".sequential")
BOT_FILE = "main.py"



def ensure_dirs():
    """Ensure base directory structure exists."""
    for category in ["tokens", "apis"]:
        for sub in ["encrypted", "key"]:
            os.makedirs(os.path.join(BASE_DIR, category, sub), exist_ok=True)


def get_paths(category: str, provider: str):
    """Return paths for key and encrypted files based on category and provider."""
    enc_dir = os.path.join(BASE_DIR, category, "encrypted")
    key_dir = os.path.join(BASE_DIR, category, "key")

    ext = ".token" if category == "tokens" else ".api"
    token_file = os.path.join(enc_dir, f".{provider.lower()}{ext}")
    key_file = os.path.join(key_dir, f".{provider.lower()}.key")

    return token_file, key_file


def generate_key(key_file: str):
    """Generate and save a new Fernet key if it doesn't exist."""
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, "wb") as f:
            f.write(key)
    with open(key_file, "rb") as f:
        return f.read()


def get_cipher(key_file: str):
    """Return a Fernet cipher object."""
    key = generate_key(key_file)
    return Fernet(key)


def save_data(data: str, category: str, provider: str):
    """Encrypt and save data (token or API key)."""
    ensure_dirs()
    token_file, key_file = get_paths(category, provider)
    cipher = get_cipher(key_file)
    encrypted = cipher.encrypt(data.strip().encode("utf-8"))
    with open(token_file, "wb") as f:
        f.write(encrypted)


def load_data(category: str, provider: str):
    """Load and decrypt data (token or API key)."""
    ensure_dirs()
    token_file, key_file = get_paths(category, provider)
    if not os.path.exists(token_file):
        return ""
    try:
        cipher = get_cipher(key_file)
        with open(token_file, "rb") as f:
            encrypted = f.read()
        return cipher.decrypt(encrypted).decode("utf-8")
    except Exception:
        return ""


def launch_bot(token: str):
    """Launch bot.py as subprocess with env var."""
    if not os.path.exists(BOT_FILE):
        messagebox.showerror("Error", f"Cannot find {BOT_FILE}")
        return

    try:
        env = os.environ.copy()
        env["DISCORD_TOKEN"] = token
        subprocess.Popen(["python", BOT_FILE], env=env)
        messagebox.showinfo("Bot Launched", "Discord bot started successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to launch bot: {e}")



def main():
    ensure_dirs()
    root = tk.Tk()
    root.title("Sequential Credential Manager")
    root.geometry("380x340")
    root.resizable(False, False)

    tk.Label(root, text="Select Type:", font=("Segoe UI", 10, "bold")).pack(pady=(10, 2))
    category_var = tk.StringVar(value="tokens")
    category_dropdown = ttk.Combobox(
        root,
        textvariable=category_var,
        values=["tokens", "apis"],
        state="readonly",
        width=25
    )
    category_dropdown.pack(pady=5)

    tk.Label(root, text="Select Provider:", font=("Segoe UI", 10, "bold")).pack(pady=(10, 2))
    provider_var = tk.StringVar(value="Discord")
    provider_dropdown = ttk.Combobox(
        root,
        textvariable=provider_var,
        values=["Discord", "OpenAI", "Google", "GitHub", "Slack", "Handler", "Other"],
        state="readonly",
        width=25
    )
    provider_dropdown.pack(pady=5)

    tk.Label(root, text="Enter Token / API Key:", font=("Segoe UI", 10, "bold")).pack(pady=(10, 2))
    data_var = tk.StringVar()
    data_entry = tk.Entry(root, textvariable=data_var, show="*", width=45)
    data_entry.pack(pady=5)

    show_data = tk.BooleanVar(value=False)

    def toggle_visibility():
        if show_data.get():
            data_entry.config(show="*")
            toggle_btn.config(text="Show")
            show_data.set(False)
        else:
            data_entry.config(show="")
            toggle_btn.config(text="Hide")
            show_data.set(True)

    def refresh_loaded_data(*_):
        loaded = load_data(category_var.get(), provider_var.get())
        data_var.set(loaded)

    def on_save():
        data = data_var.get().strip()
        if not data:
            messagebox.showwarning("Missing Data", "Please enter a token or API key.")
            return
        save_data(data, category_var.get(), provider_var.get())
        messagebox.showinfo(
            "Saved",
            f"{provider_var.get()} {category_var.get().rstrip('s').capitalize()} saved successfully."
        )

    def on_launch():
        if category_var.get() != "tokens" or provider_var.get().lower() != "discord":
            messagebox.showwarning(
                "Invalid Action",
                "Launching is only available for Discord tokens."
            )
            return
        token = data_var.get().strip()
        if not token:
            messagebox.showwarning("Missing Token", "Please enter your Discord bot token.")
            return
        launch_bot(token)

    toggle_btn = tk.Button(root, text="Show", command=toggle_visibility, width=20)
    toggle_btn.pack(pady=3)

    tk.Button(root, text="Save", command=on_save, width=20).pack(pady=3)
    tk.Button(root, text="Launch Discord Bot", command=on_launch, width=20).pack(pady=3)

    category_dropdown.bind("<<ComboboxSelected>>", refresh_loaded_data)
    provider_dropdown.bind("<<ComboboxSelected>>", refresh_loaded_data)

    refresh_loaded_data()

    root.mainloop()


if __name__ == "__main__":
    main()