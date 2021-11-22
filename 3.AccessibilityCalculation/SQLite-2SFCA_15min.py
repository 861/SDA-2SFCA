
import apsw

groupcode_list = [-9999, 707, 601, 671, 1295, 119, 1, 917, 901, 1531, 936, 536, 812, 572, 1202, 1324, 380, 758, 3637, 3498, 241, 1127, 570, 461, 1186, 1207, 661, 4742, 3383, 1552,
                  962, 429, 770, 880, 1258, 481, 1198, 4778, 730, 1143, 595, 1183, 4704, 55204, 430, 2798, 53589, 123470, 4708, 1230, 95612, 4788, 332, 1212, 1290, 1311, 4894, 4870, 53473, 600, 96881]

for groupcode in groupcode_list:
    db = apsw.Connection('sda2sfca15.sqlite')
    cursor = db.cursor()
    cursor.execute(
        f"create temp table pop_temp as SELECT * from pop WHERE pop.groupcode = {groupcode}")
    cursor.execute(
        f"create temp table doc_temp as SELECT * from doc WHERE doc.groupcode = {groupcode}")
    cursor.execute(
        f"CREATE temp table od_pop as SELECT *, ds*w ppotent from (select * from od15min join pop_temp on pop_temp.geoid = od15min.orig)")
    cursor.execute(
        f"CREATE temp table sumpop as SELECT dest, sum(ppotent) sum_pop from od_pop GROUP BY dest")
    cursor.execute(
        f"CREATE temp table doc_sumpop as SELECT * from sumpop left join doc_temp on doc_temp.id =sumpop.dest")
    cursor.execute(
        f"CREATE temp table od_pop_doc_sumpop as SELECT * from od_pop JOIN doc_sumpop on doc_sumpop.dest = od_pop.dest")
    cursor.execute(
        f"CREATE temp table ratio as SELECT *, w* att/sum_pop R from od_pop_doc_sumpop")
    cursor.execute(
        f"insert into access15 SELECT geoid, sum(R) acc15, {groupcode} from ratio GROUP BY geoid")
    db.close()
    print(groupcode)
