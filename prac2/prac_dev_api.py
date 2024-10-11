let groups = List/map Natural Text (\(i : Natural) -> "ИКБО-${Natural/show i}-20") (List/replicate 23 1 + List/replicate 23 1)

let students =
      [ { age = 19, group = groups.(3), name = "Иванов И.И." }
      , { age = 18, group = groups.(4), name = "Петров П.П." }
      , { age = 18, group = groups.(4), name = "Сидоров С.С." }
      , { age = 20, group = groups.(10), name = "Андреев А.А." }
      ]

in  { groups = groups, students = students, subject = "Конфигурационное управление" }
