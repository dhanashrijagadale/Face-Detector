import pywhatkit as pw
text="""Artificial intelligence (AI) is the ability of a computer or a robot controlled by a computer to do tasks that are usually done by humans because they require human intelligence and discernment."""
pw.text_to_handwriting(text,"handwriting.png",[0,0,138])
print("Code Completed")