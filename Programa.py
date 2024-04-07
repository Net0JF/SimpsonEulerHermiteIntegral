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
    
def function_evaluar(function_string, x):
    try:
        return float(sympify(function_string).subs('x', x))                        
    except Exception as e:
        messagebox.showerror("Error", f"Error al evaluar función: {e}")
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
           
#Interfaz para solicitar valores a usuario y evaluar la función dada por métdoo de Euler
def euler_window():
    window = tk.Toplevel()
    window.title("Euler")
    window.geometry("300x250")
    
    label_funcion = tk.Label(window, text="EDO de primer orden (dy/dx =f(x, y)): ")
    label_funcion.pack()
    entry_funcion = tk.Entry(window)
    entry_funcion.pack(pady=5)
   
    label_x0_y0 = tk.Label(window, text="Condición inicial (x0, y0): ")
    label_x0_y0.pack()
    entry_x0_y0 = tk.Entry(window)
    entry_x0_y0.pack(pady=5)
    
    label_h = tk.Label(window, text= "Paso de integración (h): ")
    label_h.pack()
    entry_h = tk.Entry(window)
    entry_h.pack(pady=5)
    
    label_n = tk.Label(window, text= "Número de pasos (n): ")
    label_n.pack()
    entry_n = tk.Entry(window)
    entry_n.pack(pady=5)

    button_calcular= tk.Button(window, text="Calcular",command=lambda: metodo_euler(entry_funcion.get(), entry_x0_y0.get(), entry_h.get(), entry_n.get()))
    button_calcular.pack(pady=5)

def metodo_euler(function_string, xy0, h, n):
    try:
        x0, y0 = map(float, xy0.split())
        h = float(h)
        n = int(n)
        result = []
        
        for _ in range(n):
            yi = y0 + h * function_evaluar(function_string, x0)
            result.append((x0, yi))
            x0 += h
            y0 = yi
        
        messagebox.showinfo("Resultado: ", f"Solución aproximada: {result}")
    except ValueError:
        messagebox.showerror("Error", "Favor de ingresar números válidos para x0, y0, h y n")

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

def metodo_hermite(puntos_str, valores_str):
    try:
        puntos = [tuple(map(float, p.split()))for p in puntos_str.split]
        valores = [float(x)for x in valores_str.split]
        result = []
        
        for x_valor in valores:
            hermite_polynomial = 0
            
            for i in range(len(puntos)):
                p, y = puntos[i]
                derivatives = [0] * len(puntos)
                h=0
                
                for j in range(len(puntos)):
                    if j==0:
                        h= puntos[j+1][0] - puntos[j][0]
                    elif j== len(puntos)-1:
                        h=puntos[j][0]-puntos[j-1][0]
                    else:
                        h = puntos[j+1][0] - puntos[j-1][0]
                        
                    function_str = function_str.replace("y", str((y)).replace("x", f"({x_valor})"))
                    derivatives[j]=(function_evaluar(function_str, p+h)-function_evaluar(function_str, p))/h
                    
                hermite_basis=1
                hermite_basis_derivative=0
                
                for j in range(len(puntos)):
                    if j!= i:
                        hermite_basis *= (x_valor - puntos[j][0])
                        hermite_basis_derivative += 1/(p-puntos[j][0])
                hermite_polynomial += y * hermite_basis * ((1-2* hermite_basis_dertivative * (x_valor-p))*(1-2*hermite_basis_derivative*(x_valor-p))-h*h*hermite_basis_derivative)/(h*h)
            result.append((x_valor, hermite_polynomial))
        
        messagebox.showinfo("Resultado", f"Interpolación de Hermite para los valores de x: {result}")
    except ValueError:
        messagebox.showerror("Error", "Ingresar puntos y valores de x válidos")
    

if __name__ == "__main__":
    main()