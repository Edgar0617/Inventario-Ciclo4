package com.misiontic.cliente_ms.repositories;
import com.misiontic.cliente_ms.models.Inventariado;
import org.springframework.data.mongodb.repository.MongoRepository;
import java.util.List;
public interface InventariadoRepository extends MongoRepository<Inventariado, String> {
    List<Inventariado> findByUsernameOrigin (String usernameOrigin);
    List<Inventariado> findByUsernameDestiny (String usernameDestiny);
}
