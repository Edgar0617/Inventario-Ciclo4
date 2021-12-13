package com.misiontic.cliente_ms.exceptions;

public class CuentaNotFoundException extends RuntimeException {
    public CuentaNotFoundException(String message) {
        super(message);
    }
}
