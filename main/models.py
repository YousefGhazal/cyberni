from django.db import models

class Certificat(models.Model):
    CERTIFICAT_CHOICES = [
        ("CISSP", "CISSP"),
        ("CISA", "CISA"),
        ("Security +", "Security +"),
        ("CEH", "CEH"),
        ("CISM", "CISM"),
        ("GSEC", "GSEC"),
        ("SSCP", "SSCP"),
        ("CASP+", "CASP+"),
        ("GCIH", "GCIH"),
        ("OSCP", "OSCP"),
        ("CTIA", "CTIA"),
        ("CHFI", "CHFI"),
        ("CND", "CND"),
        ("CF", "CF"),
        ("CRISC", "CRISC"),
        ("CySA+", "CySA+"),
        ("CCSP", "CCSP"),
        ("CSSLP", "CSSLP"),
        ("CCFP", "CCFP"),
        ("CCNA", "CCNA"),
        ("CCNP", "CCNP"),
        ("GPEN", "GPEN"),
        ("CCSK", "CCSK"),
        ("CSC", "CSC"),
        ("CFR", "CFR"),
        ("eJPT", "eJPT"),
        ("eCIR", "eCIR"),
        ("CSA", "CSA"),
        ("C|CT", "C|CT"),
        ("ECSA", "ECSA"),
    ]


class Client(models.Model):
    certificate = models.CharField(choices=CERTIFICAT_CHOICES)
    note = models.TextField()