from fpdf import FPDF 
import pandas as pd 
data=pd.read_csv("topics 1.csv",sep=',')  


pdf=FPDF(orientation='P',unit="mm",format="a4")
for imdex,row in data.iterrows(): 
    pdf.add_page() 
    pdf.set_font(family="Times",style="B",size=12,) 
    pdf.line(10,21,200,22) 

    pdf.cell(w=0,h=12,txt=row["Topic"] ,align="C",ln=1)  
    if row["Pages"] >1:
        for page in range(row["Pages"]-1): 
            pdf.add_page()
    
    
pdf.output("output.pdf")
 


#pdf.add_page()
#pdf.set_font(family="Times",style="B",size=12,)
#pdf.cell(w=0,h=12,txt="yooooo there",align="L",ln=1)
#pdf.set_font(family="Times",size=12,)
#pdf.cell(w=0,h=12,txt="Hello there",align="L",ln=2) 

