import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Calculadora matemática")
    
    label = tk.Label(root, text="Menú:")
    label.pack()
    
    button_simpson = tk.Button(root, text="Simposon compuesta", command = simpson_compuesta_window)
    button_simpson.pack
    
def simpson_compuesta_window():
    window = tk.Toplevel()
    window.title("Simpson Compuesta")
    
    label_function = tk.Label(window, text="Función a integrar (f(x)): ")
    label_function.pack()
    entry_function = tk.Entry(window)
    entry_function.pack()
    

    
    
if __name__ == "__main__":
    main()