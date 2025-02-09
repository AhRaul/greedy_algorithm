states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])   #Основной список необходимых к покрытию штатов.
                                                                            #Преобразован в массив множеств,
                                                                            #с целью, избежать повторений.
                                                                            # Предположительно, это штаты.
stations = {}                                   #Список подмножеств,  которые частично пересекаются друг с другом.
                                                    #Среди которых ведется поиск, необходимого минимума подмножеств,
                                                    # который нужен, чтобы полностью покрыть основной список множеств.
                                                    # Предположительно, это радиостанции,
                                                    # покрывающие свой участок штатов.
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()          #Финальный список, который нужно заполнить станциями, покрывающими основное множество.

while states_needed:            #Повторяем цикл, пока в главном массиве не закончатся города.
    best_station = None         #Выбираем лучший вариант станции, согласно алгоритму:
                                    # Станция покрывает как можно больше, ранее не покрытых, штатов.
    states_covered = set()      #инициализируем множество, рассматриваемой станции
    for station, states_for_station in stations.items():    #обходим все станции, и элементы внутри станций.
        covered = states_needed & states_for_station  #Записываем в covered пересечения 2-х множеств (основного, и станции)
        if len(covered) > len(states_covered):          #Если станция пересекает больше станций, чем предыдущая, в цикле.
            best_station = station                      #То, эта станция будет считаться лучшим вариантом, из оставшихся.
            states_covered = covered                    #Записываем её список покрытий, для следующего шага цикла.

    final_stations.add(best_station)    #После цикла, лучшая станция будет записана в список выбранных, и рассмотренных.
    states_needed -= states_covered     #Из главного массива городов удаляем уже рассмотренные.

print(final_stations)       #Результат работы программы, список необходимых станций для покрытия всех штатов.