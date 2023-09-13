# THIS GENERATES PDF FROM A CSV FILE

from fpdf import FPDF 
import pandas as pd 
data=pd.read_csv("topics 1.csv",sep=',')  



pdf=FPDF(orientation='P',unit="mm",format="a4") 
pdf.set_auto_page_break(auto=False,margin=0)
for imdex,row in data.iterrows(): 
    pdf.add_page() 
    pdf.set_font(family="Times",style="B",size=12,) 
    # To make a line
    for y in range(20,298,10):
        pdf.line(10,y,200,y)

    pdf.cell(w=0,h=12,txt=row["Topic"] ,align="C",ln=1)   
    pdf.ln(265) 
    # SET THE FOOTER 
    pdf.set_font(family="Times",style="I",size=8) 
    pdf.set_text_color(180,180,180) 
    pdf.cell(w=0,h=10,txt=row["Topic"],align="R")
    if row["Pages"] >1:
        for page in range(row["Pages"]-1): 
            pdf.add_page()
            pdf.ln(278) 
            # SET THE FOOTER 
            pdf.set_font(family="Times",style="I",size=8) 
            pdf.set_text_color(180,180,180) 
            pdf.cell(w=0,h=10,txt=row["Topic"],align="R") 
            for y in range(20,298,10):
                 pdf.line(10,y,200,y) 
    
    
pdf.output("output.pdf")
 


#pdf.add_page()
#pdf.set_font(family="Times",style="B",size=12,)
#pdf.cell(w=0,h=12,txt="yooooo there",align="L",ln=1)
#pdf.set_font(family="Times",size=12,)
#pdf.cell(w=0,h=12,txt="Hello there",align="L",ln=2) 

