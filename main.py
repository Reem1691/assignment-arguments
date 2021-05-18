# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

    
def greet(name,greeting_template='Hello, <name>!'):
    greeting = greeting_template.replace('<name>!', '')
    print(f'{greeting}{name}!\n')
    return f'{greeting}{name}!'


greet('Bob')
greet('Jack', 'What\'s up, ')
greet('John', "Hi there, ")


def force(mass,body='earth'):
    surface_gravity = dict([
        ('sun', 274.0),
        ('jupiter', 24.9),
        ('neptune', 11.15),
        ('saturn', 10.4),
        ('earth', 9.8),
        ('uranus', 8.9),
        ('venus', 8.9),
        ('mars', 3.7),
        ('mercury', 3.7),
        ('moon', 1.62),
        ('pluto', 0.6)
        ])
    force_exerted = mass * surface_gravity[body]
    print(f'object mass: {mass}')
    print(f'celestial body: {body}')
    print(f'The force exerted on an celestial object with mass {mass} on body {body} is {force_exerted} \n')
    return (force_exerted)


force(1.5)
force(1.5, 'moon')


def pull(m1, m2, d):
    g = 6.674 * 10 **-11
    grav_pull = g * ((float(m1) * float(m2))/(float(d)**2))
    print(f'mass of object m1 in kilogram: {m1}')
    print(f'mass of object m2 in kilogram: {m2}')
    print(f'distance between object m1 and m2 in meter: {d}')
    print(f'the gravitational pull between m1 and m2 in Newton: {grav_pull}\n')
    return grav_pull


pull(800, 1500, 3)
pull(0.1, 5.972*10**24, 6.371*10**6)


