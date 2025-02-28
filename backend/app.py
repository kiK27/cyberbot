from flask import Flask, request, jsonify, render_template
from transformers import pipeline
from flask_cors import CORS

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)  # Enable CORS for frontend requests

# Load the pre-trained BERT model for Question-Answering
qa_pipeline = pipeline("question-answering", model="deepset/bert-base-cased-squad2")

# ✅ Add a route for the homepage
@app.route("/")
def home():
    return render_template("index.html")  # Load the chatbot UI

@app.route("/chat", methods=["POST"])
def chatbot():
    data = request.json
    question = data.get("question", "").strip().lower()

    # Custom predefined responses
    greetings = {
        "hi": "Hi! How can I help you?",
        "hello": "Hello! How can I assist you?",
        "hey": "Hey there! What do you need help with?",
        "how are you": "I'm just a chatbot, but I'm here to help with your cybersecurity questions!",
        "thank you": "Your Welcome!"
    }

    # Check if the input matches a predefined response
    if question in greetings:
        return jsonify({"answer": greetings[question]})

    # Cybersecurity knowledge base (Expand this for better results)
    context = """
### **1. Phishing Attacks**
Phishing is a type of cyber attack where attackers impersonate a trusted entity to trick individuals into revealing sensitive information, such as passwords, credit card numbers, or social security numbers.  
Common phishing techniques include:  
- **Email phishing**: Fraudulent emails that mimic legitimate organizations, often containing malicious links or attachments.  
- **Spear phishing**: A more targeted form of phishing where attackers customize messages for specific individuals or organizations.  
- **Whaling**: A phishing attack directed at high-profile targets like executives or government officials.  
- **Smishing & Vishing**: Phishing attacks carried out through SMS (smishing) or phone calls (vishing).  

**Prevention Tips:**  
- Never click on links from unknown senders.  
- Check email sender addresses for authenticity.  
- Enable spam filters and multi-factor authentication (MFA).  

---

### **2. Firewalls & Network Security**
A firewall is a security device (hardware or software) that monitors and controls incoming and outgoing network traffic based on predetermined security rules.  

Types of firewalls:  
- **Packet-filtering firewall**: Inspects data packets and blocks suspicious traffic.  
- **Stateful inspection firewall**: Monitors active connections and blocks unauthorized access.  
- **Proxy firewall**: Acts as an intermediary between users and the internet for added security.  
- **Next-Generation Firewall (NGFW)**: Includes advanced features like intrusion prevention and deep packet inspection.  

**Network Security Best Practices:**  
- Use **Virtual Private Networks (VPNs)** for secure browsing.  
- Implement **intrusion detection/prevention systems (IDS/IPS)**.  
- Regularly update routers and security software.  

---

### **3. Password Security & Multi-Factor Authentication (MFA)**
A strong password should:  
- Have at least **12-16 characters**.  
- Include **uppercase, lowercase, numbers, and special characters**.  
- Avoid common words, birthdays, or personal information.  

**Best Practices for Password Security:**  
- Use a **password manager** to store and generate strong passwords.  
- Enable **Multi-Factor Authentication (MFA)**, requiring an extra step (such as a phone OTP) beyond a password.  
- Regularly **update passwords** and avoid reusing them across multiple sites.  

---

### **4. Encryption & Data Protection**
Encryption is the process of converting plaintext into unreadable ciphertext to prevent unauthorized access.  

**Common Encryption Methods:**  
- **AES (Advanced Encryption Standard)**: Used for secure data storage and communication.  
- **RSA (Rivest-Shamir-Adleman)**: A public-key encryption algorithm used for securing online transactions.  
- **End-to-End Encryption (E2EE)**: Ensures only the sender and receiver can read messages (e.g., WhatsApp, Signal).  

**Data Protection Tips:**  
- Always **encrypt sensitive data** before storing or sharing.  
- Use **secure cloud services** that offer encryption.  
- Be cautious of **public Wi-Fi**, as it can expose data to hackers.  

---

### **5. Malware: Viruses, Trojans, & Ransomware**
Malware is malicious software designed to harm or exploit devices, networks, or users.  

**Types of Malware:**  
- **Viruses**: Attach themselves to files and spread when executed.  
- **Trojans**: Disguised as legitimate software but contain malicious code.  
- **Worms**: Self-replicating programs that spread across networks.  
- **Spyware**: Secretly gathers user information.  
- **Adware**: Unwanted software that displays intrusive advertisements.  
- **Ransomware**: Encrypts a victim’s files and demands a ransom for their release.  

**Protection Against Malware:**  
- Keep **operating systems and software updated**.  
- Use **antivirus and anti-malware software**.  
- Avoid downloading files from **untrusted sources**.  

---

### **6. Social Engineering Attacks**
Social engineering manipulates people into revealing confidential information.  

**Common Social Engineering Techniques:**  
- **Pretexting**: Creating a fabricated scenario to steal information.  
- **Baiting**: Offering free software or files to lure users into downloading malware.  
- **Tailgating**: Gaining unauthorized physical access by following someone through a secured entry.  

**How to Protect Yourself:**  
- Be skeptical of **unsolicited requests for sensitive information**.  
- Verify identities before **sharing personal or company data**.  
- Train employees to recognize **social engineering attacks**.  

---

### **7. Zero-Day Vulnerabilities & Security Patches**
A **zero-day vulnerability** is a security flaw in software that is unknown to the vendor and unpatched, making it a prime target for cybercriminals.  

**How to Stay Safe:**  
- **Regularly update software and applications**.  
- Use **automatic security patches** when available.  
- Follow cybersecurity news to stay informed about **emerging threats**.  

---

### **8. Distributed Denial-of-Service (DDoS) Attacks**
A **DDoS attack** floods a website or server with excessive traffic, causing slowdowns or crashes.  

**Common DDoS Attack Types:**  
- **Volume-based attacks**: Overwhelm bandwidth capacity.  
- **Protocol attacks**: Exploit network weaknesses.  
- **Application-layer attacks**: Target specific web applications.  

**Prevention Measures:**  
- Use **DDoS mitigation services**.  
- Implement **rate limiting** to control traffic flow.  
- Monitor network activity for **suspicious spikes in traffic**.  

---

### **9. Safe Internet Browsing**
- Always verify **HTTPS** before entering sensitive data on a website.  
- Avoid **public Wi-Fi** for banking or confidential activities.  
- Be cautious of **browser extensions and plugins** that request excessive permissions.  

**Recognizing Unsafe Websites:**  
- Look for **SSL/TLS certificates** (padlock icon in browser).  
- Avoid sites with **multiple pop-ups and spelling errors**.  
- Use **web filtering tools** to block malicious sites.  

---

### **10. IoT & Smart Device Security**
The **Internet of Things (IoT)** includes smart home devices, cameras, and wearables, which can be vulnerable to cyberattacks.  

**Securing IoT Devices:**  
- Change default usernames and passwords.  
- Keep device firmware updated.  
- Disable unused features and remote access when not needed.  

---

### **11. Cybersecurity Best Practices**
- **Backup important data regularly** to prevent loss due to cyberattacks.  
- **Use VPNs** when accessing sensitive information over public networks.  
- **Educate employees** about phishing and cyber threats.  
- **Enable two-factor authentication (2FA)** for critical accounts.  

---

### **12. Incident Response & Reporting Cyber Threats**
If you suspect a cybersecurity breach:  
1. **Disconnect affected devices** from the network.  
2. **Report the incident** to IT security or law enforcement.  
3. **Change passwords** and secure accounts immediately.  
4. **Monitor for unusual activity** to prevent further damage.  

Government agencies like **CISA (Cybersecurity and Infrastructure Security Agency)** and **CERT (Computer Emergency Response Team)** can provide assistance.  
"""


    response = qa_pipeline({"question": question, "context": context})

    return jsonify({"answer": response["answer"]})

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
