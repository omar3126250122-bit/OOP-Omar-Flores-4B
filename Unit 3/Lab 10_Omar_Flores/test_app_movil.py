import pytest
from app_movil import (PerfilMovil, PerfilPro,SuscripcionExpiradaError, PuntosInsuficientesError)

@pytest.fixture
def perfil():
    return PerfilMovil("ana")

def test_valores_iniciales(perfil):
    assert perfil.username == "ana"
    assert perfil.gemas == 50
    assert perfil.racha_dias == 1
    assert perfil.notificaciones_activas is True


def test_ganar_gemas_suma(perfil):
    assert perfil.ganar_gemas(10) == 60
    assert perfil.gemas == 60


def test_gastar_gemas_resta(perfil):
    assert perfil.gastar_gemas(20) == 30
    assert perfil.gemas == 30

def test_gemas_iniciales_negativas():
    with pytest.raises(ValueError):
        PerfilMovil("ana", gemas=-5)


def test_gastar_mas_de_lo_disponible(perfil):
    with pytest.raises(PuntosInsuficientesError):
        perfil.gastar_gemas(999)


@pytest.mark.parametrize("cantidad", [0, -1])
def test_gastar_cantidad_invalida(perfil, cantidad):
    with pytest.raises(ValueError):
        perfil.gastar_gemas(cantidad)

@pytest.mark.parametrize("cantidad, esperado", [
    (1, 51),
    (10, 60),
    (100, 150),
])
def test_ganar_gemas_validas(perfil, cantidad, esperado):
    assert perfil.ganar_gemas(cantidad) == esperado


@pytest.mark.parametrize("cantidad", [0, -1, -100])
def test_ganar_gemas_invalidas(perfil, cantidad):
    with pytest.raises(ValueError):
        perfil.ganar_gemas(cantidad)

def test_perfil_pro_es_instancia_de_perfil_movil():
    pro = PerfilPro("luis", meses_suscripcion=3)
    assert isinstance(pro, PerfilPro)
    assert isinstance(pro, PerfilMovil)
    assert pro.es_pro is True
    assert pro.gemas == 50 


def test_perfil_pro_meses_invalidos():
    with pytest.raises(ValueError):
        PerfilPro("luis", meses_suscripcion=0)


def test_descarga_offline_exitosa():
    pro = PerfilPro("luis", meses_suscripcion=2)
    assert pro.descargar_contenido_offline() == "Descarga offline completada"


def test_descarga_offline_suscripcion_expirada():
    pro = PerfilPro("luis", meses_suscripcion=1)
    pro.meses_suscripcion = 0 
    with pytest.raises(SuscripcionExpiradaError):
        pro.descargar_contenido_offline()
    assert pro.es_pro is False