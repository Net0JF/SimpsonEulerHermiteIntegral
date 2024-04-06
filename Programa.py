import tkinter as tk
from tkinter import messagebox


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

    button_calcular= tk.Button(window, text="Calcular", comand=lambda: simpson_compuesta(entry_function.get(), entry_a.get(), entry_b.get, entry_n.get))
    button_calcular.pack
    
def simpson_compuesta(a, b, n):
    try:
        a = float(a)
        b = float(b)
        n = float(n)
        h = (b-a)/n
        resultado=0
        
        for i in range (n+1):
            xi = a + i * h
            ki = funcion_evaluar(funcion_String, xi)
            
            if i == 0 or i == n:
                resultado +=  ki
            elif i%2==0:
                resultado += 2*ki
            else:
                resultado += 4*ki
        resultado *= h/ 3.0
        
        messagebox.showinfo("Resultado: ", f"El resultado de la integral es: {resultado:.5f}")
        
    except ValueError:
        messagebox.showinfo("Error", "Favor de ingresar valores validos")
        
        def funcion_evaluar(funcion_String, xi)
        
    
    
if __name__ == "__main__":
    main()