package com.misiontic.cliente_ms.exceptions;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.ResponseStatus;
@ControllerAdvice
@ResponseBody
public class InsufficientGananciasAdvice {
    @ResponseBody
    @ExceptionHandler(InsufficientGananciasException.class)
    @ResponseStatus(HttpStatus.CONFLICT)
    String InsufficientBalanceAdvice(InsufficientGananciasException ex){
        return ex.getMessage();
    }
}
