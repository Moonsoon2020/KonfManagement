{
  local groups = ["ИКБО-%d-20" % i for i in std.range(1, 24)],

  groups: groups,

  students: [
    { age: 19, group: groups[3], name: "Иванов И.И." },
    { age: 18, group: groups[4], name: "Петров П.П." },
    { age: 18, group: groups[4], name: "Сидоров С.С." },
    { age: 20, group: groups[10], name: "Андреев А.А." }  // добавлен четвертый студент
  ],

  subject: "Конфигурационное управление"
}
