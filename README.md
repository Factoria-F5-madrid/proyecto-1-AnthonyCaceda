<p align="center">
  <img src="assets/freepik_assistant_1751889862952.png"
 alt="Diagrama del taxímetro" width="70%" />
</p>

enlace sitio web: https://automad-43omx79.gamma.site/#card-e4itmufxnka8ibv

# 🚘 Automad

¡Bienvenido a **Automad**!  
Un sistema interactivo de simulación de viajes 🚦 que calcula el tiempo y costo de trayectos en función de los estados: **en movimiento** y **detenido**.

---

## 🧾 Descripción

Automad es una aplicación de consola escrita en Python. Permite a los usuarios iniciar un viaje, cambiar de estado entre "detenido" y "en movimiento", y luego finalizar el viaje para calcular el costo total, basado en el tiempo transcurrido en cada estado.

---

## 🧭 Comandos Disponibles

| Comando   | Acción que realiza                        |
|-----------|--------------------------------------------|
| `start`   | Inicia un nuevo viaje.                    |
| `move`    | Cambia el estado a **en movimiento** 🚗   |
| `stop`    | Cambia el estado a **detenido** 🛑         |
| `finish`  | Finaliza el viaje y muestra el costo total 💰 |
| `exit`    | Sale del programa 👋                      |

---

## ⚙️ Funcionamiento

- Al iniciar un viaje (`start`), el estado predeterminado es `stopped`.
- Puedes alternar entre `move` y `stop`.
- El tiempo en cada estado se mide y se almacena.
- Al finalizar (`finish`), se calcula el costo total:
  
  | Estado       | Tarifa por segundo |
  |--------------|--------------------|
  | ⏸️ Stopped    | **0.02 €**         |
  | ▶️ Moving     | **0.05 €**         |

---

## 💻 Ejemplo de Uso

```plaintext
¡Hi, welcome to Automad!
Thank you for using our services, here is a list of keywords to use in our program: start, move, stop, finish and exit.

:start
Trip started. Initial state: 'stopped'.

:move
State changed to 'moving'.

:stop
State changed to 'stopped'.

:move
State changed to 'moving'.

:finish
**************************
total:  0.273 €
**************************

:exit
Exiting the program. Goodbye!
```
---
 
## 🔮 Futuras Implementaciones
```plaintext
💾 Guardar historial
Registro en archivo .csv, .json o base de datos.
```
```plaintext
🖼️ Interfaz gráfica (GUI)
Usar Tkinter, PyQt o interfaz web para experiencia visual.
```
```plaintext
📊 Exportar recibos
Generar informes PDF o recibos con resumen del viaje.
```
```plaintext
🔐 Multiusuario
Añadir login para usuarios y viajes personalizados.
```
```plaintext
🛠️ Parámetros configurables
Cambiar tarifas desde archivo de configuración.
```
```plaintext
🌍 Idiomas
Soporte multilingüe (español, inglés, etc.)
```
```plaintext
📉 Simulación visual
Mostrar progreso del viaje con barras o animaciones en consola o GUI.
```
```plaintext
🧪 Testing
Añadir pruebas unitarias para mayor confiabilidad.
```
## 🧑‍💻 Autor
Desarrollado por Anthony Caceda
