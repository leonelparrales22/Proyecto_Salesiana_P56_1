
CREATE TABLE USUARIOS (
                cedula_usuario VARCHAR(10) NOT NULL,
                contrasenia VARCHAR(25) NOT NULL,
                rol VARCHAR(6) NOT NULL,
                PRIMARY KEY (cedula_usuario)
);


CREATE TABLE CLIENTE (
                cedula_cliente VARCHAR(10) NOT NULL,
                nombre_cliente VARCHAR(30) NOT NULL,
                apellido_cliente VARCHAR(30) NOT NULL,
                direccion_cliente VARCHAR(100) NOT NULL,
                PRIMARY KEY (cedula_cliente)
);


CREATE TABLE VENTAS (
                codigo_venta VARCHAR(36) NOT NULL,
                cedula_cliente VARCHAR(10) NOT NULL,
                cedula_usuario VARCHAR(10) NOT NULL,
                fecha DATETIME NOT NULL,
                PRIMARY KEY (codigo_venta)
);


CREATE TABLE FACTURA (
                id_factura VARCHAR(36) NOT NULL,
                codigo_venta VARCHAR(36) NOT NULL,
                subtotal DECIMAL(5,2) NOT NULL,
                descuento DECIMAL(5,2) NOT NULL,
                iva DECIMAL(5,2) NOT NULL,
                total DECIMAL(5,2) NOT NULL,
                observaciones VARCHAR(1000) NOT NULL,
                PRIMARY KEY (id_factura)
);


CREATE TABLE CELULARES (
                id_celular VARCHAR(36) NOT NULL,
                nombre_celular VARCHAR(150) NOT NULL,
                marca_celular VARCHAR(50),
                stock_celular INT NOT NULL,
                precio_celular DECIMAL(5,2) NOT NULL,
                PRIMARY KEY (id_celular)
);


CREATE TABLE DETALLE_VENTA (
                codigo_venta VARCHAR(36) NOT NULL,
                id_celular VARCHAR(36) NOT NULL,
                cantidad INT NOT NULL
);


ALTER TABLE VENTAS ADD CONSTRAINT usuarios_ventas_fk
FOREIGN KEY (cedula_usuario)
REFERENCES USUARIOS (cedula_usuario)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE VENTAS ADD CONSTRAINT cliente_ventas_fk
FOREIGN KEY (cedula_cliente)
REFERENCES CLIENTE (cedula_cliente)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE FACTURA ADD CONSTRAINT ventas_factura_fk
FOREIGN KEY (codigo_venta)
REFERENCES VENTAS (codigo_venta)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE DETALLE_VENTA ADD CONSTRAINT ventas_detalle_venta_fk
FOREIGN KEY (codigo_venta)
REFERENCES VENTAS (codigo_venta)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE DETALLE_VENTA ADD CONSTRAINT celulares_detalle_venta_fk
FOREIGN KEY (id_celular)
REFERENCES CELULARES (id_celular)
ON DELETE NO ACTION
ON UPDATE NO ACTION;


INSERT INTO celulares VALUES("9eee0e45-cdff-4d2d-baae-b64592af0c81","iPhone 6S 32GB","APPLE",12,227);
INSERT INTO celulares VALUES("7b79a50f-bbb5-4d56-a7dd-ac7f4eb59d26","iPhone 6S 64GB","APPLE",5,277);
INSERT INTO celulares VALUES("b99cc16d-a2ce-4bc4-a9c5-d727479ba5b9","iPhone 6S 128GB","APPLE",8,297);


INSERT INTO celulares VALUES("c3a32237-d969-4dbc-a875-0ae6ae544e35","iPhone 7 32GB","APPLE",4,317);
INSERT INTO celulares VALUES("380f7194-029f-4e79-bad3-788cf25491be","iPhone 7 128GB","APPLE",2,367);



INSERT INTO celulares VALUES("dfefa9cd-79e2-4cf0-a9bf-3edfabab87b5","iPhone 7 Plus 32GB","APPLE",5,447);
INSERT INTO celulares VALUES("8a811cda-c695-4d48-b293-6cd68e306e50","iPhone 7 Plus 128GB","APPLE",8,497);
INSERT INTO celulares VALUES("34737c5d-de37-448f-b120-c5c1b613d83c","iPhone 7 Plus 256GB","APPLE",3,527);



INSERT INTO celulares VALUES("5fabef97-5624-46c9-ac1b-4921660fda68","iPhone 8 64GB","APPLE",5,447);
INSERT INTO celulares VALUES("6514f137-ab23-4e15-8ca9-0c0ee7c6d880","iPhone 8 256GB","APPLE",4,497);



INSERT INTO celulares VALUES("2c985fd8-64db-42ee-8e9c-4adcb002e3ef","iPhone 8 Plus 64GB","APPLE",10,577);
INSERT INTO celulares VALUES("5b2a3d39-fc57-4a67-bf15-a8f9d10aa335","-iPhone 8 Plus 128GB","APPLE",5,617);
INSERT INTO celulares VALUES("7fe0f0de-10b7-4d80-8163-07a61b0512fa","iPhone 8 Plus 256GB","APPLE",7,647);

