from battery_dispatch.simulate import simulate


def main():
    battery = simulate()
    print(
        f"Final Battery Charge: {battery.charge:.2f} MW, "
        f"Final Balance: £{battery.balance:.2f}"
    )

if __name__ == "__main__":
    main()
