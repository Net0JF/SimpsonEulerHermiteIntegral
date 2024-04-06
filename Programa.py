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
    
    button_euler = tk.Button(root, text="Euler", command = euler_window)
    button_euler.pack(pady=5)
    
    button_hermite = tk.Button(root, text="Interpolación de Hermite", command = hermite_window)
    button_hermite.pack(pady=5)
    
    button_salir = tk.Button(root, text="Salir", command=root.destroy)
    button_salir.pack(pady=5)
    
    root.mainloop()
    
def simpson_compuesta(function_string, a, b, n):
    try:
        a = float(a)
        b = float(b)
        n = int(n)
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
        messagebox.showinfo("Resultado", f"El resultado de la integral es: {resultado:.5f}")       
        
    except ValueError:
        messagebox.showinfo("Error", "Favor de ingresar valores validos")
        
def function_evaluar(function_string, x):
    try:
        return float(sympify(function_string).subs('x', x))                        
    except Exception as e:
        messagebox.showerror("Error", f"Erroe al evaluar función: {e}")
        return 0  
    
#Interfaz para solicitar valores a usuario y evaluar la función dada mediante el algoritmo de Simpson compuesta
def simpson_compuesta_window():
    window = tk.Toplevel()
    window.title("Simpson Compuesta")
    window.geometry("300x250")
    
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

    button_calcular= tk.Button(window, text="Calcular", command=lambda: simpson_compuesta(entry_function.get(), entry_a.get(), entry_b.get(), entry_n.get()))
    button_calcular.pack(pady=5)
    
#Interfaz para solicitar valores a usuario y evaluar la función dada
def euler_window():
    window = tk.Toplevel()
    window.title("Euler")
    window.geometry("300x250")
    
    label_function = tk.Label(window, text="EDO de primer orden (dy/dx =f(x, y)): ")
    label_function.pack()
    entry_function = tk.Entry(window)
    entry_function.pack(pady=5)
    
    label_a = tk.Label(window, text="Condición inicial (x0, y0): ") 
    label_a.pack()
    entry_a = tk.Entry(window)
    entry_a.pack(pady=5)
    
    label_b = tk.Label(window, text= "LPaso de integración (h): ")
    label_b.pack()
    entry_b = tk.Entry(window)
    entry_b.pack(pady=5)
    
    label_n = tk.Label(window, text= "Número de pasos (n): ")
    label_n.pack()
    entry_n = tk.Entry(window)
    entry_n.pack(pady=5)

    #button_calcular= tk.Button(window, text="Calcular", command=lambda: metodo_euler(entry_function.get(), entry_x0_y0.get(), entry_h.get(), entry_n.get()))
    #button_calcular.pack(pady=5)

def metodo_euler():
    try
    except



def hermite_window():
    window = tk.Toplevel()
    window.title("Hermite")
    window.geometry("300x250")
    
    label_puntos = tk.Label(window, text="Conjunto de puntos (x, y): ")
    label_puntos.pack()
    entry_puntos = tk.Entry(window)
    entry_puntos.pack(pady=5)
    
    label_x_valores = tk.Label(window, text="Valores de x para interpolar") 
    label_x_valores.pack()
    entry_x_valores = tk.Entry(window)
    entry_x_valores.pack(pady=5)

    button_calcular= tk.Button(window, text="Calcular", command=lambda: metodo_hermite(entry_puntos.get(), entry_x_valores.get()))
    button_calcular.pack(pady=5)

def metodo_hermite():
    try
    except
    

if __name__ == "__main__":
    main()