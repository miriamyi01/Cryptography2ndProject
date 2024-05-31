import importlib
import threading

ml_kem = importlib.import_module('ML-KEM')
ml_dsa = importlib.import_module('ML-DSA')
slh_dsa = importlib.import_module('SLH-DSA')


ml_kem.perform_key_encapsulation('ML-KEM-512')
ml_kem.perform_key_encapsulation('ML-KEM-768')
ml_kem.perform_key_encapsulation('ML-KEM-1024')
ml_dsa.realizar_firma_y_verificacion('ML-DSA-44')
ml_dsa.realizar_firma_y_verificacion('ML-DSA-65')
ml_dsa.realizar_firma_y_verificacion('ML-DSA-87')
slh_dsa.realizar_firma_y_verificacion("SPHINCS+-SHA2-128f-simple")
slh_dsa.realizar_firma_y_verificacion('SPHINCS+-SHA2-192f-simple')
slh_dsa.realizar_firma_y_verificacion('SPHINCS+-SHA2-256f-simple')