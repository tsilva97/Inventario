
/*Criacao da base de dados do armario2, com os campos:
  ->name : Nome do que esta nessa gaveta do armario
  ->drawer : Numero da gaveta em que esta guardado
  ->quantity : Numero de pecas guardadas na gaveta

  A instrucao PRIMARY KEY(name, drawer) indica que a combinacao name e drawer sao uma chave da
    tabela, ou seja nao pode estar na tabela dois elementos com o mesmo nome na mesma gaveta*/

CREATE TABLE armario2(
    name varchar(80) not null,
    drawer int not null,
    quantity int not null,
    PRIMARY KEY(name, drawer)
);

/*Introducao dos dados na tabela (os paramentros estao na ordem definida em cima)

===============================================================================================
=================IMPORTANTE XXX: INTRODUZIR SEMPRE OS NOMES EM LETRA PEQUENA ==================
=================E SEM CARATERES ESPCIAIS!! ===================================================
===============================================================================================*/

INSERT INTO armario2 VALUES ('potenciometro', 1, 23);
INSERT INTO armario2 VALUES ('potenciometro', 2, 17);
INSERT INTO armario2 VALUES ('buzzer', 3, 45);
INSERT INTO armario2 VALUES ('switch', 4, 28);
INSERT INTO armario2 VALUES ('push button', 5, 243);
INSERT INTO armario2 VALUES ('capas push button', 6, 29);
INSERT INTO armario2 VALUES ('diodos', 7, 138);
INSERT INTO armario2 VALUES ('transistor tjb', 8, 4);
INSERT INTO armario2 VALUES ('condensador ceramico', 9, 17);
INSERT INTO armario2 VALUES ('condensador ceramico', 10, 95);
INSERT INTO armario2 VALUES ('condensador electrolitico (0.1-0.5 uf)', 11, 26);
INSERT INTO armario2 VALUES ('condensador electrolitico (1-5 uf)', 12, 81);
INSERT INTO armario2 VALUES ('condensador electrolitico (10-50 uf)', 13, 55);
INSERT INTO armario2 VALUES ('condensador electrolitico (100 uf)', 14, 18);
INSERT INTO armario2 VALUES ('condensador electrolitico (200 uf)', 15, 9);
INSERT INTO armario2 VALUES ('ldr (sensor de luz)', 16, 87);
INSERT INTO armario2 VALUES ('resistencias (1-9.9 ohm)', 17, 257);
INSERT INTO armario2 VALUES ('resistencias (10-99 ohm)', 18, 116);
INSERT INTO armario2 VALUES ('resistencias (100-990 ohm)', 19, 146);
INSERT INTO armario2 VALUES ('resistencias (100-990 ohm)', 20, 162);
INSERT INTO armario2 VALUES ('resistencias (1k-9.9k ohm)', 21, 140);
INSERT INTO armario2 VALUES ('resistencias (1k-9.9k ohm)', 22, 118);
INSERT INTO armario2 VALUES ('resistencias (10k-99k ohm)', 23, 171);
INSERT INTO armario2 VALUES ('resistencias (10k-99k ohm)', 24, 145);
INSERT INTO armario2 VALUES ('resistencias (100k-990k ohm)', 25, 225);
INSERT INTO armario2 VALUES ('resistencias (100k-990k ohm)', 26, 101);
INSERT INTO armario2 VALUES ('resistencias (1m - 9.9m ohm)', 27, 33);
INSERT INTO armario2 VALUES ('potenciometro (analogico)', 28, 2);
INSERT INTO armario2 VALUES ('sensor nivel de agua', 29, 1);
INSERT INTO armario2 VALUES ('sensor barometrico/altitude/temperatura', 30, 1);
INSERT INTO armario2 VALUES ('sensor de humidade do solo', 31, 1);
INSERT INTO armario2 VALUES ('amplificador de sinal (balanca)', 32, 1);
INSERT INTO armario2 VALUES ('micro sd reader', 33, 1);
INSERT INTO armario2 VALUES ('led receptor ip', 34, 25);
INSERT INTO armario2 VALUES ('led rgb', 35, 90);
INSERT INTO armario2 VALUES ('led branco', 36, 252);
INSERT INTO armario2 VALUES ('led azul', 37, 179);
INSERT INTO armario2 VALUES ('led vermelho', 38, 221);
INSERT INTO armario2 VALUES ('led amarelo', 39, 206);
INSERT INTO armario2 VALUES ('led verde', 40, 252);
INSERT INTO armario2 VALUES ('reles', 41, 20);
