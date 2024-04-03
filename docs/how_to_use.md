# How to use


## Load data

Having a file `people.csv` with the following format:

```csv
Jim Halpert, Sales, Salesman, jim@dundlermifflin.com
Dwight Schrute, Sales, Manager, schrute@dundlermifflin.com
Gabe Lewis, Director, Manager, glewis@dundlermifflin.com
```

Run `dundie load` command

```py
dundie load people.csv
```

## Viewing data

### Viewing all information

```bash
$ dundie show
                            Dunder Mifflin Report
┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ name           ┃ dept     ┃ role     ┃ email           ┃ balance ┃ last_movement   ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
│ Jim Halpert    │ Sales    │ Salesman │ jim@dundermif…  │ 3000    │ 2022-03-15T13:… │
│ Dwight Schrute │ Sales    │ Manager  │ schrute@dunde…  │ 2400    │ 2022-03-15T13:… │
│ Gabe Lewis     │ Director │ Manager  │ glewis@dunder…  │ 500     │ 2022-03-15T13:… │
└────────────────┴──────────┴──────────┴─────────────────┴─────────┴─────────────────┘
```

### Filtering

Available filters are `--dept` and `--email`

```bash
dundie show --dept=Sales
                            Dunder Mifflin Report
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ email                    ┃ name           ┃ dept  ┃ role     ┃ balance ┃ last_movement              ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ jim@dundermifflin.com    │ Jim Halpert    │ Sales │ Salesman │ 500     │ 2024-03-28T16:26:58.286204 │
│ dwight@dundermifflin.com │ Dwight Schrute │ Sales │ Manager  │ 100     │ 2024-03-28T16:26:58.286204 │
└──────────────────────────┴────────────────┴───────┴──────────┴─────────┴────────────────────────────┘
```

> **NOTE** passing `--output=file.json` will save a json file with the results.


## Adding points

An admin user can easily add points to any user or dept.

```bash
dundie add 100 --email=jim@dundlermifflin.com
                                        Report
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃ name        ┃ dept  ┃ role     ┃ email              ┃ balance ┃ last_movement      ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ Jim Halpert │ Sales │ Salesman │ jim@dundermiffli…  │ 3100    │ 2022-03-15T17:14:… │
└─────────────┴───────┴──────────┴────────────────────┴─────────┴────────────────────┘

```

Available selectors are `--email` and `--department`