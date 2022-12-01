# ODOO

## Índice

1. Instalación de nuevo módulo
2. Modelos
3. Vistas
    - Vista form
    - Vista tree
    - Vista graph
    - Vista search
4. Acciones
5. Filtros
6. Menús
7. Log de errores

<a name="item1"></a>
## Instalación de nuevo módulo

* Usamos `odoo scaffold nombre_modulo` para crear la estructura del módulo.
* Editamos el archivo `__manifest__.py` desde PyCharm.
* Reiniciamos servicio de Odoo con `systemclt restart odoo`.
* Activamos modo desarrollador con `?debug=1`.
* Actualizamos lista de aplicaciones.
* Buscamos nuestro módulo y lo instalamos.

#### Cambio icono por defecto

Creamos unha ruta `static/description` en el proyecto y añadimos una imagen con nombre `icon.png`.


## Modelos

Cabecera:

````python
class informacion(models.Model):
    _name = 'odoo_basico.informacion'
    _description = 'Exemplo para información'
````

Atributos correspondientes a campos de la tabla en BD:

````python
name = fields.Char(string="Título:")
description = fields.Text(string="Descripción:")
peso = fields.Float(string="Peso:", default=4.5)
sexo_traducido = fields.Selection([('Mujer', 'Muller'), ('Hombre', 'Home'), ('Otros', 'Outros')], string='Sexo')
autorizado = fields.Boolean(string="¿Autorizado?", default=True)
literal = fields.Char(compute='_avisoAlto', string='Literal', store=False)
alto_en_cm = fields.Integer(string="Alto en cm:")
ancho_en_cm = fields.Integer(string="Ancho en cm:")
longo_en_cm = fields.Integer(string="Longo en cm:")
volume = fields.Float(compute="_volume", store=True, string="Volume en m3")
densidade = fields.Float(compute="_densidade", store=True, string='Densidade en kg/m3')
foto = fields.Binary(string='Foto')
adxunto_nome = fields.Char(string="Nome Adxunto")
adxunto = fields.Binary(string="Arquivo adxunto")
````

Computables:

**@api.depends**
````python
@api.depends('alto_en_cm', 'longo_en_cm', 'ancho_en_cm')
def _volume(self):
    for rexistro in self:
        rexistro.volume = float(rexistro.alto_en_cm) * float(rexistro.longo_en_cm) * float(
            rexistro.ancho_en_cm) / 1000000
````
**@api.onchange**
````python
@api.onchange('alto_en_cm')
def _avisoAlto(self):
    for rexistro in self:
        if rexistro.alto_en_cm > 7:
            rexistro.literal = 'O alto ten un valor posiblemente excesivo %s é maior que 7' % rexistro.alto_en_cm
        else:
            rexistro.literal = ""
````
**@api.constrains**
````python
@api.constrains('peso')  # Ao usar ValidationError temos que importar a libreria ValidationError
def _constrain_peso(self):  # from odoo.exceptions import ValidationError
    for rexistro in self:
        if rexistro.peso < 1 or rexistro.peso > 10:
            raise ValidationError('Os peso de %s ten que ser entre 1 e 4 ' % rexistro.name)
````

## Vistas

### Vista form

````xml

<record model="ir.ui.view" id="NOMBRE_FICHERO_form_view">
    <field name="name">NOMBRE_FICHERO.form</field>
    <field name="model">NOMBRE_PROYECTO.NOMBRE_FICHERO</field>
    <field name="arch" type="xml">
        <form string="Formulario">
            <group>
                <field name="name"/>
            </group>
            <notebook>
                <page string="NOMBRE_PESTAÑA">
                    <group>
                        <field name="description"/>
                        ...
                    </group>
                </page>
                ...
            </notebook>
        </form>
    </field>
</record>
````

### Vista tree

Vista tree simple:

````xml

<record model="ir.ui.view" id="NOMBRE_FICHERO_tree_view">
    <field name="name">NOMBRE_FICHERO.tree</field>
    <field name="model">NOMBRE_PROYECTO.NOMBRE_FICHERO</field>
    <field name="arch" type="xml">
        <tree string="Árbol">
            <field name="name"/>
            ...
        </tree>
    </field>
</record>
````

Vista tree con colores:

````xml

<record model="ir.ui.view" id="NOMBRE_FICHERO_tree_view">
    <field name="name">NOMBRE_FICHERO.tree</field>
    <field name="model">NOMBRE_PROYECTO.NOMBRE_FICHERO</field>
    <field name="arch" type="xml">
        <tree string="Formulario para suceso"
              editable="top"
              decoration-success="nivel == 'Baixo'"
              decoration-warning="nivel == 'Medio'"
              decoration-danger="nivel == 'Alto'">
            <field name="name"/>
            ...
        </tree>
    </field>
</record>
````

### Vista graph

````xml

<record model="ir.ui.view" id="NOMBRE_FICHERO_graph_view">
    <field name="name">NOMBRE_FICHERO.graph</field>
    <field name="model">NOMBRE_PROYECTO.NOMBRE_FICHERO</field>
    <field name="arch" type="xml">
        <graph string="alto_en_cm" type="bar">
            <field name="alto_en_cm" type="row"/>
        </graph>
    </field>
</record>
````

### Vista search

````xml

<record model="ir.ui.view" id="NOMBRE_FICHERO_search_view">
    <field name="name">NOMBRE_FICHERO.search</field>
    <field name="model">NOMBRE_PROYECTO.NOMBRE_FICHERO</field>
    <field name="arch" type="xml">
        <search>
            <field name="name"/>
            ...
        </search>
    </field>
</record>
````

## Acciones

````xml

<record model="ir.actions.act_window" id="NOMBRE_FICHERO_list_action">
    <field name="name">TITULO_DE_NAVEGACION</field>
    <field name="res_model">NOMBRE_PROYECTO.NOMBRE_FICHERO</field>
    <field name="view_mode">tree,form,graph</field> <!-- vistas a través de las cuales funcionará la acción -->
    <field name="help" type="html"><!-- HTML por defecto cuando no hay ningún registro -->
        <p class="o_view_nocontent_smiling_face">
            Tes que crear o primeiro rexistro
        </p>
    </field>

</record>
````

## Filtros

````xml

<record model="ir.filters" id="ID_FILTRO">
    <field name="name">TITULO_FILTRO</field>
    <field name="model_id">NOMBRE_PROYECTO.NOMBRE_FICHERO</field>
    <field name="context">{'group_by': ['autorizado']}</field> <!-- Campo de agrupamiento -->
    <field name="is_default">true
    </field> <!-- Aplica este filtro por defecto; el resto de filtros deben estar a false -->
    <field name="active">true</field>
    <field name="sort">[]</field>
    <field name="domain"> <!-- Aquí iría o filtro -->
        ['|','&amp;',('autorizado', '=', False),('sexo_traducido', '=', 'Mujer'),('name', '=','Rexistro 3' )]
    </field>
    <field name="user_id"></field><!-- En blanco para que esté dispoñible para todos os usuarios -->
    <field name="action_id"
           eval="ref('NOMBRE_PROYECTO.NOMBRE_FICHERO_list_action')"/><!-- Obtemos o id a partir do id externo-->
</record>
````

## Menús

#### Menú principal

````xml

<menuitem id="ID"
          name="Menú nivel 0."/>
````

#### Submenús

````xml

<menuitem id="ID"
          name="Menú nivel 1."
          parent="ID_DEL_PADRE"
          action="ID_DE_ACCION"/>
````

## LOG

Accedemos al log de errores a través de la ruta:

```shell
tail /var/log/odoo/odoo-server.log
```