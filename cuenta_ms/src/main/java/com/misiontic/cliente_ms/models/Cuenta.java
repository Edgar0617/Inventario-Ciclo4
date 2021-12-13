package com.misiontic.cliente_ms.models;
import org.springframework.data.annotation.Id;
import java.util.Date;
public class Cuenta {
    @Id
    private String username;
    private Integer ganancias;
    private Date lastChange;
    public Cuenta(String username, Integer ganancias, Date lastChange) {
        this.username = username;
        this.ganancias = ganancias;
        this.lastChange = lastChange;
    }
    public String getUsername() {
        return username;
    }
    public void setUsername(String username) {
        this.username = username;
    }
    public Integer getGanancias() {
        return ganancias;
    }
    public void setGanancias(Integer balance) {
        this.ganancias = balance;
    }
    public Date getLastChange() {
        return lastChange;
    }
    public void setLastChange(Date lastChange) {
        this.lastChange = lastChange;
    }
}
