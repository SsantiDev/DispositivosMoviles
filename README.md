# Loyalty Rewards System

A professional, full-stack solution designed to enhance customer engagement through a robust points-accumulation and redemption ecosystem. This system provides a seamless bridge between purchase transactions and loyalty benefits, featuring a high-performance backend and a modern, "Cyber-Premium" user interface.

## Description

The **Loyalty Rewards System** is an automated platform that allows customers to accumulate value-based points for every purchase recorded. It provides a centralized dashboard where users can monitor their real-time balance, view transaction history, and redeem their accumulated rewards for monetary value. The project architecture prioritizes data integrity, precise business logic execution, and a state-of-the-art user experience.

## Business Logic

The system operates on a strictly defined mathematical model to ensure financial consistency and clear customer expectations:

- **Point Accumulation**: For every **$1,000 COP** spent in a purchase, the customer earns **1 loyalty point**. 
    - *Calculation method*: Integer division (`purchase_amount // 1000`).
- **Point Redemption**: Each accumulated point holds a tangible value. When a customer chooses to redeem their points, each **1 point** is equivalent to **$100 COP** in benefits.
    - *Redemption rule*: Users can only redeem points if their current balance meets or exceeds the requested amount.

## Tech Stack

This project leverages a modern, scalable, and highly-typed technical ecosystem:

- **Backend Architecture**:
  - **Django**: High-level Python Web framework for rapid and secure development.
  - **Django REST Framework (DRF)**: Powerful and flexible toolkit for building Web APIs, handling serialization and standardized error responses.
- **Frontend Architecture**:
  - **React**: A JavaScript library for building interactive user interfaces.
  - **TypeScript**: Ensuring type safety and enterprise-grade code maintainability across the frontend layers.
  - **Tailwind CSS**: A utility-first CSS framework for rapid UI development (integrated with custom glassmorphism and cyber-neon aesthetic modules).

---
*Developed with a focus on precision, security, and visual excellence.*

## Installation Guide

Follow these steps to set up the development environment on your local machine.

### Backend Setup (Django)
1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/macOS
   source .venv/bin/activate
   ```
3. Install project dependencies:
   ```bash
   pip install -r ..\requirements.txt
   ```
4. Perform database migrations:
   ```bash
   python manage.py migrate
   ```
5. Create an administrative user:
   ```bash
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup (React + Vite)
1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Launch the development server:
   ```bash
   npm run dev
   ```

## Naming Conventions

To ensure high-performance collaboration and code clarity, this project adheres to strict naming standards:

- **Python/Django**: Uses `snake_case` for variables, functions, and file names (e.g., `total_points`, `record_purchase`).
- **TypeScript/React**: Uses `camelCase` for variables, hooks, and logic functions (e.g., `useRewards`, `fetchBalance`).
- **Global Architecture**: Uses `PascalCase` for classes and React components (e.g., `RewardSerializer`, `RewardsDashboard`).

## Language Standards

In compliance with international technical requirements, **100% of the source code**, including variable names, class definitions, function logic, and inline documentation (comments), is written exclusively in **English**. 

All user-facing messages delivered via the API are also standardized in English to ensure a professional and unified developer experience.

## 🔌 API Endpoints

The following endpoints are available under the base path `/api/rewards/`:

| Method | Endpoint URL | Description |
| :--- | :--- | :--- |
| **GET** | `/balance/` | Retrieves the current point balance and transaction history for the user. |
| **POST** | `/purchase/` | Records a purchase amount and calculates earned points (+$1,000 = 1 pt). |
| **POST** | `/redeem/` | Deducts a specified amount of points from the balance (1 pt = -$100). |

## ⚠️ Error Handling

The API uses standard HTTP status codes and a consistent JSON format to communicate errors. This ensures that the frontend and external consumers receive clear, actionable feedback.

### Validation Errors (400 Bad Request)
If the request body contains invalid data—such as non-numeric values for `amount`, negative numbers, or missing required fields—the API returns a `400 Bad Request` response.

**Example: Invalid Data Type**
If you send `"amount": "not_a_number"`, the system responds with:
```json
{
    "error": "A valid number is required.",
    "code": "validation_error"
}
```

### Business Logic Errors (400 Bad Request)
Specific business rules are enforced at the application layer. The most common scenario is an attempt to redeem more points than what is currently available.

**Example: Insufficient Points**
If a user with a balance of `0` points attempts to redeem `10` points, the API returns:
```json
{
    "error": "Cannot redeem 10 points. Current balance is 0.",
    "code": "insufficient_points"
}
```

> [!IMPORTANT]
> Always check the `code` field in the response to implement specific UI logic (e.g., showing a specific warning modal when the code is `insufficient_points`).

---
---

# Sistema de Recompensas de Lealtad

Una solución profesional full-stack diseñada para mejorar el compromiso del cliente mediante un ecosistema robusto de acumulación y redención de puntos. Este sistema proporciona un puente fluido entre las transacciones de compra y los beneficios de lealtad, contando con un backend de alto rendimiento y una interfaz de usuario moderna "Cyber-Premium".

## Descripción

El **Sistema de Recompensas de Lealtad** es una plataforma automatizada que permite a los clientes acumular puntos basados en el valor de cada compra registrada. Proporciona un panel centralizado donde los usuarios pueden monitorear su saldo en tiempo real, ver el historial de transacciones y redimir sus recompensas acumuladas por valor monetario. La arquitectura del proyecto prioriza la integridad de los datos, la ejecución precisa de la lógica de negocio y una experiencia de usuario de vanguardia.

## Lógica de Negocio

El sistema opera bajo un modelo matemático estrictamente definido para asegurar la consistencia financiera y expectativas claras para el cliente:

- **Acumulación de Puntos**: Por cada **$1,000 COP** gastados en una compra, el cliente gana **1 punto de lealtad**.
    - *Método de cálculo*: División entera (`purchase_amount // 1000`).
- **Redención de Puntos**: Cada punto acumulado tiene un valor tangible. Cuando un cliente elige redimir sus puntos, cada **1 punto** equivale a **$100 COP** en beneficios.
    - *Regla de redención*: Los usuarios solo pueden redimir puntos si su saldo actual es igual o superior a la cantidad solicitada.

## Tecnologías

Este proyecto utiliza un ecosistema técnico moderno, escalable y altamente tipado:

- **Arquitectura Backend**:
  - **Django**: Framework web de Python de alto nivel para un desarrollo rápido y seguro.
  - **Django REST Framework (DRF)**: Herramienta potente y flexible para construir APIs Web, manejando la serialización y respuestas de error estandarizadas.
- **Arquitectura Frontend**:
  - **React**: Biblioteca de JavaScript para construir interfaces de usuario interactivas.
  - **TypeScript**: Garantiza la seguridad de tipos y el mantenimiento del código a nivel empresarial en las capas del frontend.
  - **Tailwind CSS**: Framework de CSS basado en utilidades para el desarrollo rápido de UI (integrado con módulos personalizados de estética glassmorphism y cyber-neon).

---
*Desarrollado con un enfoque en la precisión, la seguridad y la excelencia visual.*

## Guía de Instalación

Sigue estos pasos para configurar el entorno de desarrollo en tu máquina local.

### Configuración del Backend (Django)
1. Navega al directorio `backend`:
   ```bash
   cd backend
   ```
2. Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/macOS
   source .venv/bin/activate
   ```
3. Instala las dependencias del proyecto:
   ```bash
   pip install -r ..\requirements.txt
   ```
4. Realiza las migraciones de la base de datos:
   ```bash
   python manage.py migrate
   ```
5. Crea un usuario administrador:
   ```bash
   python manage.py createsuperuser
   ```
6. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

### Configuración del Frontend (React + Vite)
1. Navega al directorio `frontend`:
   ```bash
   cd frontend
   ```
2. Instala las dependencias:
   ```bash
   npm install
   ```
3. Inicia el servidor de desarrollo:
   ```bash
   npm run dev
   ```

## Convenciones de Nomenclatura

Para asegurar una colaboración de alto rendimiento y claridad en el código, este proyecto se adhiere a estándares estrictos de nomenclatura:

- **Python/Django**: Utiliza `snake_case` para variables, funciones y nombres de archivos (ej: `total_points`, `record_purchase`).
- **TypeScript/React**: Utiliza `camelCase` para variables, hooks y funciones de lógica (ej: `useRewards`, `fetchBalance`).
- **Arquitectura Global**: Utiliza `PascalCase` para clases y componentes de React (ej: `RewardSerializer`, `RewardsDashboard`).

## Estándares de Idioma

En cumplimiento con los requerimientos técnicos internacionales, el **100% del código fuente**, incluyendo nombres de variables, definiciones de clases, lógica de funciones y documentación interna (comentarios), está escrito exclusivamente en **inglés**.

Todos los mensajes orientados al usuario entregados a través de la API también están estandarizados en inglés para asegurar una experiencia de desarrollo profesional y unificada.

## 🔌 Endpoints de la API

Los siguientes endpoints están disponibles bajo la ruta base `/api/rewards/`:

| Método | URL del Endpoint | Descripción |
| :--- | :--- | :--- |
| **GET** | `/balance/` | Obtiene el saldo actual de puntos y el historial de transacciones del usuario. |
| **POST** | `/purchase/` | Registra el monto de una compra y calcula los puntos ganados (+$1,000 = 1 pt). |
| **POST** | `/redeem/` | Deduce una cantidad específica de puntos del saldo (1 pt = -$100). |

## ⚠️ Manejo de Errores

La API utiliza códigos de estado HTTP estándar y un formato JSON consistente para comunicar errores. Esto asegura que el frontend y los consumidores externos reciban retroalimentación clara y accionable.

### Errores de Validación (400 Bad Request)
Si el cuerpo de la petición contiene datos inválidos —como valores no numéricos para `amount`, números negativos o campos obligatorios faltantes— la API devuelve una respuesta `400 Bad Request`.

**Ejemplo: Tipo de Dato Inválido**
Si envías `"amount": "no_es_un_numero"`, el sistema responde:
```json
{
    "error": "A valid number is required.",
    "code": "validation_error"
}
```

### Errores de Lógica de Negocio (400 Bad Request)
Las reglas de negocio específicas se aplican en la capa de la aplicación. El escenario más común es un intento de redimir más puntos de los disponibles actualmente.

**Ejemplo: Puntos Insuficientes**
Si un usuario con un saldo de `0` puntos intenta redimir `10` puntos, la API devuelve:
```json
{
    "error": "Cannot redeem 10 points. Current balance is 0.",
    "code": "insufficient_points"
}
```

> [!IMPORTANT]
> Siempre verifica el campo `code` en la respuesta para implementar lógica específica en la UI (ej: mostrar un modal de advertencia específico cuando el código es `insufficient_points`).
