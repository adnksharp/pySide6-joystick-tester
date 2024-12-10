# Reading joysticks

![](https://i.imgur.com/vYC2GBK.png)

Lectura de joysticks para revisar problemas de drift con arduino y pySide6.

## Requisitos

[FirmataExpress](https://mryslab.github.io/pymata4/firmata_express/#installation-instructions)

### Librerías de Python

- PySide6
- pymata4
- matlotlib

```bash
pip install -r requirements.txt
```

### Hardware usado

| ![](https://i.imgur.com/bCuJUrt.png) | ![](https://i.imgur.com/GpTIpTK.png) |
|----|----|

- Placa de Arduino MEGA 2560.
- Modulo de joystick para Arduino.

## Características
- Graficar la lectura de un joystick en `x`, `y`, dentro de un scatterplot.
- Mostrar los valores del joystick en lcdnumbers.

### En proceso

> [!TIP]
>
> - Lectura de varios joysticks a la vez.
