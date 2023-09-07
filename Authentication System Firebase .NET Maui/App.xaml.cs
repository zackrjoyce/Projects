using Firebase.Auth;
using Firebase.Auth.Providers;
using Firebase.Auth.Repository;
using Firebase.Database;
using Google.Apis.Auth.OAuth2;

namespace MauiTestApp
{
    public partial class App : Application
    {
        public FirebaseAuthClient authClient;
        public FirebaseClient firebaseClient;
        public App()
        {
            InitializeComponent();

            // Configure...
            var config = new FirebaseAuthConfig
            {
                ApiKey = "AIzaSyCLItvscxOuAATopsWRA6RYY9wuKcF5dyU",
                AuthDomain = "snooz-auth-demo.firebaseapp.com",
                Providers = new FirebaseAuthProvider[]
                {
                    // Add and configure individual providers
                    new GoogleProvider().AddScopes("email"),
                    new EmailProvider()
                    // ...
                },
                // WPF:
                UserRepository = new FileUserRepository("FirebaseSample") // persist data into %AppData%\FirebaseSample
            };

            // ...and create your FirebaseAuthClient
            authClient = new FirebaseAuthClient(config);

            firebaseClient = new FirebaseClient("https://snooz-auth-demo-default-rtdb.firebaseio.com/");

            MainPage = new AppShell();
        }
    }
}