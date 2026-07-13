import subprocess
from groq import Groq
from datetime import datetime

target = input("Target IP: ")

print("\nScanning in Progress\n")
result = subprocess.run(
    ["nmap", "-sV", target],
    capture_output=True,
    text=True
)
scan_output = result.stdout

print("NMAP RAW OUTPUT")
print(scan_output)

client = Groq()

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": f"""Ye ek nmap scan ka result hai. Isko ek pentester ke liye simple summary mein samjhao.

IMPORTANT: Plain text mein jawab do, koi Markdown formatting use mat karo. No hash symbols, no asterisks, no bullet points ke liye special symbols. Sirf normal numbers aur simple sentences use karo.

Format:
1. Kaunsi services chal rahi hain
2. Kaunsi purani ya vulnerable ho sakti hain
3. Priority order mein bata do kya pehle check karna chahiye

Scan data:
{scan_output}
"""
        }
    ]
)

ai_analysis = response.choices[0].message.content

print("AI ANALYSIS")
print(ai_analysis)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
report_filename = f"report_{target}_{timestamp}.txt"

with open(report_filename, "w") as f:
    f.write("  AI-POWERED RECON & VULNERABILITY TRIAGE REPORT\n")
    f.write(f"Target IP       : {target}\n")
    f.write(f"Scan Date/Time  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"Tool Used       : Nmap 7.99 + Groq AI (llama-3.3-70b)\n")
    f.write("SECTION 1: RAW NMAP SCAN OUTPUT\n")
    f.write(scan_output)
    f.write("SECTION 2: AI RISK ANALYSIS & PRIORITY RECOMMENDATIONS\n")
    f.write(ai_analysis)
    f.write("  END OF REPORT\n")

print(f"\nReport saved: {report_filename}")
