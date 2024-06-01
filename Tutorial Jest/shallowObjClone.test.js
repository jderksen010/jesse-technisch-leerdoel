const shallowObjClone = require('./shallowObjClone');

test('Create a clone of the object parameter', () => {
    const myObj = { person: "Hitchmaker", number: 42 };
    expect(shallowObjClone(myObj)).toStrictEqual(myObj);
});