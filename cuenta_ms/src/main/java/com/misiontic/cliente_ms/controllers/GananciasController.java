package com.misiontic.cliente_ms.controllers;

import com.misiontic.cliente_ms.exceptions.CuentaNotFoundException;
import com.misiontic.cliente_ms.exceptions.InsufficientGananciasException;
import com.misiontic.cliente_ms.models.Cuenta;
import com.misiontic.cliente_ms.models.Inventariado;
import com.misiontic.cliente_ms.repositories.CuentaRepository;
import com.misiontic.cliente_ms.repositories.InventariadoRepository;
import org.springframework.web.bind.annotation.*;
import java.util.Date;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;
@RestController
public class GananciasController {
    private final CuentaRepository cuentaRepository;
    private final InventariadoRepository inventariadoRepository;
    public GananciasController(CuentaRepository cuentaRepository,
                                 InventariadoRepository transactionRepository) {
        this.cuentaRepository = cuentaRepository;
        this.inventariadoRepository = transactionRepository;
    }
    @PostMapping("/transactions")
    Inventariado newInventariado(@RequestBody Inventariado inventariado){
        Cuenta cuentaOrigin =
                cuentaRepository.findById(inventariado.getUsernameOrigin()).orElse(null);
        Cuenta cuentaDestinity=
                cuentaRepository.findById(inventariado.getUsernameDestiny()).orElse(null);
        if (cuentaOrigin == null)
            throw new CuentaNotFoundException("No se encontro una cuenta con el username: " + inventariado.getUsernameOrigin());
        if (cuentaDestinity == null)
            throw new CuentaNotFoundException("No se encontro una cuenta con el username: " + inventariado.getUsernameDestiny());
        if(cuentaOrigin.getGanancias() < inventariado.getValue())
            throw new InsufficientGananciasException("Ganancias Insuficientes");
        cuentaOrigin.setGanancias(cuentaOrigin.getGanancias() - inventariado.getValue());
        cuentaOrigin.setLastChange(new Date());
        cuentaRepository.save(cuentaOrigin);
        cuentaDestinity.setGanancias(cuentaDestinity.getGanancias() +
                inventariado.getValue());
        cuentaDestinity.setLastChange(new Date());
        cuentaRepository.save(cuentaDestinity);
        inventariado.setDate(new Date());
        return inventariadoRepository.save(inventariado);
    }
    @GetMapping("/inventariado/{username}")
    List<Inventariado> userTransaction(@PathVariable String username){
        Cuenta userCuenta = cuentaRepository.findById(username).orElse(null);
        if (userCuenta == null)
            throw new CuentaNotFoundException("No se encontró una cuenta con el username: " + username);
                    List<Inventariado> transactionsOrigin =
                            inventariadoRepository.findByUsernameOrigin(username);
        List<Inventariado> inventariadoDestinity =
                inventariadoRepository.findByUsernameDestiny(username);
        List<Inventariado> inventariado = Stream.concat(transactionsOrigin.stream(),
                inventariadoDestinity.stream()).collect(Collectors.toList());
        return inventariado;
    }
}
