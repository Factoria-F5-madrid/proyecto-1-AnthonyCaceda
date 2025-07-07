🚗 Automad
Automad es un programa interactivo en Python que simula un sistema de seguimiento de viajes con estados de movimiento (moving) y detención (stopped). Calcula automáticamente el costo total del viaje en función del tiempo que el vehículo ha estado en cada estado.

🧠 Descripción del Proyecto
Este programa fue diseñado como una herramienta simple de simulación para calcular tarifas de viaje dependiendo del tiempo en movimiento y detenido. El usuario puede controlar el viaje mediante comandos y el sistema calculará el costo según los siguientes criterios:

Cada segundo detenido (stopped) cuesta 0.02 €

Cada segundo en movimiento (moving) cuesta 0.05 €

▶️ Comandos Disponibles
El programa reconoce los siguientes comandos:

Comando	Descripción
start	Inicia un nuevo viaje. Estado inicial: stopped.
move	Cambia el estado actual a moving.
stop	Cambia el estado actual a stopped.
finish	Finaliza el viaje y calcula el costo total.
exit	Sale del programa.

🧪 Ejemplo de Uso
plaintext
Copiar
Editar
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
🧩 Lógica Interna del Programa
Estados: El viaje tiene dos estados posibles: stopped y moving.

Temporización: Usa time.time() para medir los segundos en cada estado.

Cálculo: Al finalizar (finish), se multiplica el tiempo por las tarifas asignadas para calcular el total.

🛠️ Tecnologías Usadas
Python 3.x

Módulo time para medición de intervalos

💡 Posibles Mejoras Futuras
Persistencia de Datos
Guardar un historial de viajes en un archivo (.csv, .json o base de datos).

Interfaz Gráfica (GUI)
Usar Tkinter, PyQt o web para una interfaz más amigable.

Exportar Recibos
Permitir guardar el recibo del viaje con detalles como:

Tiempo detenido

Tiempo en movimiento

Costo total

Fecha/hora de inicio y fin

Validaciones más robustas
Manejo de errores más detallado (por ejemplo, evitar finish dos veces seguidas).

Soporte multilingüe
Agregar soporte para varios idiomas usando un sistema de localización.

Sistema de autenticación
Permitir que diferentes usuarios puedan iniciar sesión y llevar su propio historial de viajes.

Simulación visual del estado actual
Mostrar gráficamente el cambio entre stopped y moving durante la ejecución.

Parámetros configurables
Permitir modificar las tarifas por segundo desde un archivo de configuración.
