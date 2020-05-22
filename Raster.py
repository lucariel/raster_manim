
import pandas as pd
class Raster(VMobject):
    def __init__(self, datos, *vmobjects, **kwargs):
        if not all([isinstance(m, VMobject) for m in vmobjects]):
            raise Exception("All submobjects must be of type VMobject")
        
        if not isinstance(datos, pd.DataFrame):
            raise Exception("Data is not a Data Frame with columns(names) = [x,y,layer]")


        VMobject.__init__(self, **kwargs)
        self.res = int(np.sqrt(datos.shape[0]))
        self.colores = ["#B91E17","#F74006","#F77006","#F7A706","#F6ED6A","#F8FBA2","#E0FBA2","#A2FBC2","#A2DBFB","#1CACFD","#08689E"]
        self.datos = datos.sort_values(['x', 'y'], ascending=[False, False]).pivot('y', 'x', 'layer').values

        rs = []
        for i in range(self.res):
            for j in range(self.res):
                value = self.datos[j][i]
                col = self.get_color_raster(value,self.colores)
                r=Rectangle(height=0.02,width=0.02, color=col, fill_color = col,fill_opacity=1).move_to(DOWN*(3.0-(j*0.02))+LEFT*(6-(i*0.02)))
                rs.append(r)

        self.add(*rs)
    def get_color_raster(self,value, colores, range_values=[0,100], range_step = 10):
        range_values_list=[]
        for i in range(range_values[0],range_values[1],range_step):
            range_values_list.append(i)
        if value == range_values_list[0]:
            col = "#000000"
        elif value > range_values_list[0] and value < range_values_list[1]:
            col = colores[0]
        elif value >=range_values_list[1]  and value < range_values_list[2]:
            col = colores[1]
        elif value >=range_values_list[2]  and value < range_values_list[3]:
            col = colores[2]
        elif value >=range_values_list[3]  and value < range_values_list[4]:
            col = colores[3]
        elif value >=range_values_list[4]  and value < range_values_list[5]:
            col = colores[4]
        elif value >=range_values_list[5]  and value < range_values_list[6]:
            col = colores[5]
        elif value >=range_values_list[6]  and value < range_values_list[7]:
            col = colores[6]
        elif value >=range_values_list[7]  and value < range_values_list[8]:
            col = colores[7]
        elif value >=range_values_list[8]  and value < range_values_list[9]:
            col = colores[8]
        elif value >=range_values_list[9]:
            col = colores[9]
        return col
                



