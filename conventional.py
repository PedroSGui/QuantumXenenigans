import pandapower as pp

def create_ieee_6bus_system():
    net = pp.create_empty_network()

    # Create buses
    bus_data = [(0, 138), (1, 138), (2, 138), (3, 69), (4, 69), (5, 69)]
    for b in bus_data:
        pp.create_bus(net, vn_kv=b[1], name=f"Bus {b[0] + 1}")

    # Create external grid
    pp.create_ext_grid(net, bus=0)

    # Create generators
    gen_data = [(1, 0), (2, 1), (3, 2)]
    for g in gen_data:
        pp.create_gen(net, bus=g[1], p_mw=g[0], vm_pu=1.0)

    # Create loads
    load_data = [(0.9, 3), (0.9, 4), (0.9, 5)]
    for l in load_data:
        pp.create_load(net, bus=l[1], p_mw=l[0])

    # Create lines
    line_data = [(0, 1, 0.10, 0.20), (0, 3, 0.05, 0.20), (0, 4, 0.08, 0.30), (1, 2, 0.05, 0.25), (1, 5, 0.10, 0.35), (2, 3, 0.05, 0.12), (2, 4, 0.05, 0.20), (3, 5, 0.03, 0.08)]
    for line in line_data:
        pp.create_line_from_parameters(net, from_bus=line[0], to_bus=line[1], length_km=1, r_ohm_per_km=line[2], x_ohm_per_km=line[3], c_nf_per_km=0, max_i_ka=1)

    # Create transformers
    trafo_data = [(1, 4, 0.10, 0.4), (2, 5, 0.08, 0.2)]
    for trafo in trafo_data:
        pp.create_transformer_from_parameters(net, hv_bus=trafo[0], lv_bus=trafo[1], sn_mva=1, vn_hv_kv=138, vn_lv_kv=69, vkr_percent=trafo[2], vk_percent=trafo[3], pfe_kw=0, i0_percent=0)

    return net

# Test the create_ieee_6bus_system function
if __name__ == "__main__":
    net = create_ieee_6bus_system()
    
    # Run power flow
    pp.runpp(net)

    # Print results
    print("\nBus Results:")
    print(net.res_bus)

    print("\nLine Results:")
    print(net.res_line)

    print("\nTransformer Results:")
    print(net.res_trafo)

    print("\nGenerator Results:")
    print(net.res_gen)

    print("\nLoad Results:")
    print(net.res_load)
