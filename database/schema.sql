CREATE DATABASE motivio;

USE motivio;

CREATE TABLE vehicles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    make VARCHAR(255) NOT NULL,
    model VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    vin VARCHAR(255) NOT NULL,
    mileage INT NOT NULL
);

CREATE TABLE maintenance_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id INT NOT NULL,
    service_type VARCHAR(255) NOT NULL,
    service_date DATE NOT NULL,
    mileage INT NOT NULL,
    notes TEXT,
    receipt_url VARCHAR(255),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(id)
);