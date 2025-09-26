from django.db import models


class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True,
    )

    created_at = models.DateTimeField(  # Quando foi criado
        db_column='created_at',
        auto_now_add=True,
        null=False,
    )

    modified_at = models.DateTimeField(  # Última modificação
        db_column='modified_at',
        auto_now=True,
        null=False,
    )
    active = models.BooleanField(  # Se está ativo ou não
        db_column='cs_active',
        default=True,
        null=False,
    )

    class Meta:
        abstract = True
        managed = False


class Author(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        max_length=255,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f'{self.id} - {self.name}'  # Quando for listado exibirá id e nome da pessoa

    class Meta:
        db_table = 'author'
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
