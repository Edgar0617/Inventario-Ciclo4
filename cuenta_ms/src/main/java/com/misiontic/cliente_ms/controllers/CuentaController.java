package com.misiontic.cliente_ms.controllers;

import com.misiontic.cliente_ms.exceptions.CuentaNotFoundException;
import com.misiontic.cliente_ms.models.Cuenta;
import com.misiontic.cliente_ms.repositories.CuentaRepository;
import org.springframework.web.bind.annotation.*;
@RestController
public class CuentaController {
    private final CuentaRepository cuentaRepository;
    public CuentaController(CuentaRepository accountRepository) {
        this.cuentaRepository = accountRepository;
    }
    @GetMapping("/accounts/{username}")
    Cuenta getAccount(@PathVariable String username){
        return cuentaRepository.findById(username)
                .orElseThrow(() -> new CuentaNotFoundException("No se encontró una cuenta con el username: " + username));
    }
    @PostMapping("/accounts")
    Cuenta newCuenta(@RequestBody Cuenta cuenta){
        return cuentaRepository.save(cuenta);
    }
}
