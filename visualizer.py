import matplotlib.pyplot as pt
import seaborn as sb
def visualize(df):
    print("Generating histogram: ")
    df.hist()
    pt.show()
    print("Generating heatmap: ")
    sb.heatmap(df.corr())
    pt.show()