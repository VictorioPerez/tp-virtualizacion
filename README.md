# Trabajo Práctico – Virtualización con VirtualBox

**Materia:** Arquitectura y Sistemas Operativos
**Alumnos:** Victorio Perez
**Fecha de entrega:** 18/11/2026

## Resumen

Se configuró Oracle VirtualBox, se instaló una distribución Linux (Ubuntu o Linux Mint) en una máquina virtual y se ejecutó una aplicación en Python que calcula el promedio de tres notas.

## Contenido del repositorio

| Archivo / carpeta | Descripción |
|---|---|
| `informe-tecnico.pdf` | Informe con los conceptos teóricos y los procedimientos realizados. |
| `promedio.py` | Código fuente de la aplicación desarrollada. |
| `capturas/` | Capturas de pantalla del proceso y de los resultados. |
| `README.md` | Esta guía. |

## Cómo ejecutar el programa

1. Abrir una terminal en la máquina virtual Linux.
2. Verificar que Python esté instalado:
   ```bash
   python3 --version
   ```
   Si no está disponible:
   ```bash
   sudo apt update
   sudo apt install -y python3
   ```
3. Ejecutar el programa desde la carpeta del repositorio:
   ```bash
   python3 promedio.py
   ```
4. Ingresar las tres notas cuando el programa las pida.

## Ejemplo de ejecución

```
Ingrese la nota 1: 7
Ingrese la nota 2: 8
Ingrese la nota 3: 9
El promedio es: 8.00
```

## Entorno utilizado

- Anfitrión (host): Windows 11
- Hipervisor: Oracle VirtualBox
- Invitado (guest): Ubuntu
- Recursos de la VM: 2 GB de memoria, 25GB de disco
