import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_luo_nollatilavuuden_negatiivisella_arvolla(self):
        varasto = Varasto(-1)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_konstruktori_luo_nollasaldon_negatiivisella_arvolla(self):
        varasto = Varasto(0, -5)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_negatiivisena_ei_lisaa_saldoa(self):
        alkusaldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-23)
        
        self.assertAlmostEqual(self.varasto.saldo, alkusaldo)

    def test_lisays_yli_mahtuvuuden_asettaa_saldoksi_tilavuuden(self):
        tilavuus = self.varasto.tilavuus
        lisaysmaara = tilavuus + 100
        self.varasto.lisaa_varastoon(lisaysmaara)

        self.assertAlmostEqual(self.varasto.saldo, tilavuus)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ottaminen_negatiivisella_arvolla_palauttaa_nollan(self):
        self.varasto.lisaa_varastoon(8)
        paluuarvo = self.varasto.ota_varastosta(-1234)

        self.assertAlmostEqual(paluuarvo, 0)

    def test_ottaminen_yli_saldon_antaa_koko_saldon(self):
        self.varasto.lisaa_varastoon(43232)
        saldo_ennen_ottoa = self.varasto.saldo
        enemman_kuin_saldo = self.varasto.saldo + 1234
        kaikki_mita_saatiin = self.varasto.ota_varastosta(enemman_kuin_saldo)

        self.assertAlmostEqual(kaikki_mita_saatiin, saldo_ennen_ottoa)

    def test_ottaminen_yli_saldon_asettaa_saldoksi_nollan(self):
        self.varasto.lisaa_varastoon(43232)
        enemman_kuin_saldo = self.varasto.saldo + 1234
        self.varasto.ota_varastosta(enemman_kuin_saldo)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_varaston_merkkijonoesitys_on_oikean_muotoinen(self):
        self.varasto.lisaa_varastoon(913765)

        oletettu_merkkijonomuoto = f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}"

        self.assertEqual(str(self.varasto), oletettu_merkkijonomuoto)
    
