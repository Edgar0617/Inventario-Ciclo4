package com.misiontic.cliente_ms.repositories;
import com.misiontic.cliente_ms.models.Cuenta;
import org.springframework.data.mongodb.repository.MongoRepository;
public interface CuentaRepository extends MongoRepository <Cuenta, String> { }
