import analyzer
import loader
import visualizer
def main():
    filepath = input("Enter file path: ")
    df = loader.load_csv(filepath)
    if df is None:
        return
    analyzer.analyze(df)
    visualizer.visualize(df)
if __name__ == "__main__":
    main()

