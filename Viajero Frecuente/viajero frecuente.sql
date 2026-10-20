-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Viajero frecuente
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Viajero frecuente
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Viajero frecuente` DEFAULT CHARACTER SET utf8 ;
USE `Viajero frecuente` ;

-- -----------------------------------------------------
-- Table `Viajero frecuente`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Viajero frecuente`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(250) NULL,
  `apellido` VARCHAR(250) NULL,
  `email` VARCHAR(250) NULL,
  `password` VARCHAR(250) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Viajero frecuente`.`destinos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Viajero frecuente`.`destinos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `destino` VARCHAR(250) NULL,
  `inicio` DATETIME NULL,
  `fin` DATETIME NULL,
  `itinerario` TEXT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Viajero frecuente`.`inscripciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Viajero frecuente`.`inscripciones` (
  `usuario_id` INT NOT NULL,
  `destino_id` INT NOT NULL,
  PRIMARY KEY (`usuario_id`, `destino_id`),
  INDEX `fk_usuarios_has_destinos_destinos1_idx` (`destino_id` ASC) VISIBLE,
  INDEX `fk_usuarios_has_destinos_usuarios_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_usuarios_has_destinos_usuarios`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `Viajero frecuente`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_usuarios_has_destinos_destinos1`
    FOREIGN KEY (`destino_id`)
    REFERENCES `Viajero frecuente`.`destinos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;