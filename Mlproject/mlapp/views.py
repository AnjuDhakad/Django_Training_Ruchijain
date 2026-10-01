from django.shortcuts import render
import joblib


# Home Page
def home(request):
    return render(request, 'home.html')


# Result Page
def result(request):

    # Load trained scaler and ML model
    scaler = joblib.load('scalermodel.pkl')
    mlmodel = joblib.load('mlmodel.pkl')

    # Get input values
    lis = []

    lis.append(float(request.POST['RI']))
    lis.append(float(request.POST['Na']))
    lis.append(float(request.POST['Mg']))
    lis.append(float(request.POST['AL']))
    lis.append(float(request.POST['Si']))
    lis.append(float(request.POST['K']))
    lis.append(float(request.POST['Ca']))
    lis.append(float(request.POST['Ba']))
    lis.append(float(request.POST['Fe']))

    # Scale input
    scaled_input = scaler.transform([lis])

    # Predict
    ans = mlmodel.predict(scaled_input)[0]

    # Convert number into glass name
    glass_types = {
        1: "Building Windows Float Processed",
        2: "Building Windows Non-Float Processed",
        3: "Vehicle Windows Float Processed",
        4: "Vehicle Windows Non-Float Processed",
        5: "Containers",
        6: "Tableware",
        7: "Headlamps"
    }

    # Get glass name
    glass_name = glass_types.get(int(ans), "Unknown Glass Type")

    # Send result to result.html
    return render(
        request,
        'result.html',
        {
            'ans': glass_name,
            'lis': lis
        }
    )