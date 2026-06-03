from collections import defaultdict

def compute_metrics(events):

    visitors = set()

    section_visitors = {
        "ZONE_1": set(),
        "ZONE_2": set(),
        "BILLING": set()
    }

    for e in events:

        visitors.add(e.visitor_id)

        if e.event_type == "ZONE_ENTER":

            if e.zone_id == "ZONE_1":
                section_visitors["ZONE_1"].add(e.visitor_id)

            elif e.zone_id == "ZONE_2":
                section_visitors["ZONE_2"].add(e.visitor_id)

            elif e.zone_id == "BILLING":
                section_visitors["BILLING"].add(e.visitor_id)

    total_visitors = len(visitors)

    return {
        "total_visitors": total_visitors,

        "zone_1": len(section_visitors["ZONE_1"]),
        "zone_2": len(section_visitors["ZONE_2"]),
        "billing": len(section_visitors["BILLING"])
    }