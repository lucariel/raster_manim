
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
