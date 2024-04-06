import tkinter as tk
from tkinter import messagebox

from sympy import sympify


def main():
    root = tk.Tk()
    root.title("Calculadora matemática")
    root.geometry("300x200")
    
    label = tk.Label(root, text="Menú:")
    label.pack()
    
    button_simpson = tk.Button(root, text="Simposon compuesta", command = simpson_compuesta_window)
    button_simpson.pack(pady=5)
    
    button_salir = tk.Button(root, text="Salir", command=root.destroy)
    button_salir.pack(pady=5)
    
    root.mainloop()
    
def simpson_compuesta(function_string, a, b, n):
    try:
        a = float(a)
        b = float(b)
        n = float(n)
        h = (b-a)/n
        resultado=0
        
        for i in range (n+1):
            xi = a + i * h
            ki = function_evaluar(function_string, xi)
            
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
        
def function_evaluar(function_string, x):
    try:
        return float(sympify(function_string).subs('x', x))                        
    except Exception as e:
        messagebox.showerror("Error", f"Erroe al evaluar función: {e}")
        return 0  
    
def simpson_compuesta_window():
    window = tk.Toplevel()
    window.title("Simpson Compuesta")
    window.geometry("200x250")
    
    label_function = tk.Label(window, text="Función a integrar (f(x)): ")
    label_function.pack()
    entry_function = tk.Entry(window)
    entry_function.pack(pady=5)
    
    label_a = tk.Label(window, text="Límite inferior (a): ") 
    label_a.pack()
    entry_a = tk.Entry(window)
    entry_a.pack(pady=5)
    
    label_b = tk.Label(window, text= "Límite inferior (b): ")
    label_b.pack()
    entry_b = tk.Entry(window)
    entry_b.pack(pady=5)
    
    label_n = tk.Label(window, text= "Número de intervalos (n): ")
    label_n.pack()
    entry_n = tk.Entry(window)
    entry_n.pack(pady=5)

    button_calcular= tk.Button(window, text="Calcular", command=lambda: simpson_compuesta(entry_function.get(), entry_a.get(), entry_b.get, entry_n.get()))
    button_calcular.pack(pady=5) 

            
if __name__ == "__main__":
    main()