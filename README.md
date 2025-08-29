<h1 align="center">🛡️ Argus</h1>
<p align="center">
  <strong>Directory & Subdomain Enumerator + DNS Recon Tool</strong><br>
  <em>Keep an eye on the internet like the all-seeing Argus</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-active-brightgreen" alt="status">
  <img src="https://img.shields.io/badge/language-python-blue" alt="language">
  <img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="license">
</p>

---

## 🔍 About Argus

**Argus** is a fast, modular, and flexible tool designed for reconnaissance and information gathering. Whether you're mapping out a target's directories, hunting for subdomains, or retrieving DNS records like `A`, `AAAA`, `CNAME`, `MX`, and more — **Argus** has your back.

### ✨ Features

- 🌐 Subdomain Enumeration 
- 📁 Directory Brute-forcing 
- 📄 DNS Record Lookup (`A`, `AAAA`, `MX`, `CNAME`, `NS`, `TXT`, etc.)
- 🧩 Modular Architecture – use what you need
- ⚡ Fast and lightweight
- 💾 Output to file support

---

## ⚙️ Installation

### 📦 1. Clone the Repository

```bash
git clone https://github.com/yourusername/argus.git
cd Argus
```

### 🐍 2. Set Up a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 📥 3. Download Requirements

```bash
pip install -r requirements.txt
```

### 🛠️ Install Argus Globally (Optional)

(Keep in mind, for this to work, you will have to install the requirements globally with sudo pip install requirements.txt)
```bash
chmod +x argus.py
sudo ln -s $(pwd)/argus.py /usr/local/bin/argus
```

Now you can simply run:
```bash
argus -h
```

---

## 🚀 Usage

Run `argus` with various flags depending on what kind of scan you'd like to perform.

```bash
argus [action] example.com [options]
```

<img width="869" height="297" alt="Screenshot 2025-08-29 at 19 07 46" src="https://github.com/user-attachments/assets/c9ca7cf1-ec0b-4c4b-9bec-524c1e3c7ab8" />

---

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome!

If you'd like to contribute to **Argus**, follow these steps:

1. 🍴 Fork the repository
2. 🛠️ Create a new branch (`git checkout -b feature/your-feature-name`)
3. 🧪 Make your changes and test them
4. 📩 Submit a pull request

Please follow best practices and include clear commit messages.

> For major changes, open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more details.

---

## 🙏 Credits

- Inspired by tools like `sublist3r`, `dirsearch`, and `dnsenum`
- Built with ❤️ using Python 3
- Special thanks to the open-source community

---

## 🧭 Roadmap

- [ ] Add support for reverse DNS lookups
- [ ] Built-in wordlists auto-fetch option
- [ ] Output to CSV and HTML reports
- [ ] Subdomain takeover detection
- [ ] Plugin system for extending modules

---

## 📬 Support

If you find this tool helpful, feel free to:

- ⭐ Star the repo to show your support
- 🐞 Open an issue if you encounter bugs
- 🧠 Suggest features via [Issues](../../issues)

---

## 📌 Disclaimer

This tool is intended for **educational and authorized security testing purposes only**.  
**Do not** use Argus against systems without permission.  
The developer is not responsible for any misuse or damages.

---





