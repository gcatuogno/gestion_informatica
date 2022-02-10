from fpdf import FPDF
import datetime

class PDF(FPDF):
    def header(self):
        # Logo
        #self.image('assetes\icons\logo_pb.png', 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Productos Bajos de Stock', 0, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# Funcion que permite exportar el pedido a PDF. 
def exportRequest(data):
    
    # Extraemos la fehca y hora.
    fecha = datetime.datetime.now()
    fecha = "{}-{}-{} H{};{}".format(fecha.day, fecha.month, fecha.year, fecha.hour, fecha.minute)
    
    # Creamos el nombre del archivo y generamos el PDF.
    requestName = "Pedido del {}.pdf".format(fecha)
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 8)
    for i in data:
        pdf.cell(0, 10, "Descripcion: {}, Codigo: {}, Cantidad {}, Proveedor: {} ".format(i[1], i[2], i[3], i[4]), 0, 1)
    pdf.output(requestName , 'F')
    print("Exportacion realziada con exito")
