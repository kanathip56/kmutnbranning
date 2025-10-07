<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FitTracker Thailand - คำนวณแคลอรี่การออกกำลังกาย</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {
            box-sizing: border-box;
        }
        .gradient-bg {
            background: linear-gradient;
        }
        .card-shadow {
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }
        .animate-bounce-slow {
            animation: bounce 2s infinite;
        }
        .chart-container {
            position: relative;
            height: 300px;
            width: 100%;
        }
        .autocomplete-dropdown {
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: white;
            border: 1px solid #d1d5db;
            border-top: none;
            border-radius: 0 0 0.5rem 0.5rem;
            max-height: 200px;
            overflow-y: auto;
            z-index: 1000;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }
        .autocomplete-item {
            padding: 0.75rem 1rem;
            cursor: pointer;
            border-bottom: 1px solid #f3f4f6;
        }
        .autocomplete-item:hover {
            background-color: #f3f4f6;
        }
        .autocomplete-item.selected {
            background-color: #dbeafe;
            color: #1d4ed8;
        }
        .custom-location {
            background-color: #fef3c7;
            border-left: 3px solid #f59e0b;
        }
    </style>
</head>
<body class="gradient-bg min-h-screen">
    <!-- Login/Register Screen -->
    <div id="loginScreen" class="min-h-screen flex items-center justify-center p-4">
        <div class="bg-white rounded-2xl card-shadow p-8 w-full max-w-4xl">
            <div class="text-center mb-8">
                <!-- Language Selector -->
                <div class="flex justify-end mb-4">
                    <select id="languageSelector" class="px-3 py-2 border border-gray-300 rounded-lg text-sm">
                        <option value="th">🇹🇭 ไทย</option>
                        <option value="en">🇺🇸 English</option>
                    </select>
                </div>
                
                <h1 id="appTitle" class="text-4xl font-bold text-gray-800 mb-2">🏃‍♂️ FitTracker Thailand</h1>
                <p id="appSubtitle" class="text-gray-600">ระบบคำนวณแคลอรี่การออกกำลังกาย</p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <!-- Login Form -->
                <div class="space-y-6">
                    <h2 class="text-2xl font-bold text-gray-800 text-center" data-translate="login">เข้าสู่ระบบ</h2>
                    
                    <form id="loginForm" class="space-y-4">
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-2" data-translate="username">ชื่อผู้ใช้</label>
                            <input type="text" id="loginUsername" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent" placeholder="กรอกชื่อผู้ใช้">
                        </div>
                        
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-2" data-translate="password">รหัสผ่าน</label>
                            <input type="password" id="loginPassword" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent" placeholder="กรอกรหัสผ่าน">
                        </div>
                        
                        <button type="submit" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded-lg transition duration-200" data-translate="loginBtn">
                            เข้าสู่ระบบ
                        </button>
                    </form>
                    
                    <div class="text-center">
                        <p class="text-sm text-gray-600" data-translate="demoText">ทดลองใช้: username: <strong>demo</strong>, password: <strong>1234</strong></p>
                    </div>
                </div>
                
                <!-- Register Form -->
                <div class="space-y-6 border-l border-gray-200 pl-8">
                    <h2 class="text-2xl font-bold text-gray-800 text-center" data-translate="register">สมัครสมาชิก</h2>
                    
                    <form id="registerForm" class="space-y-4">
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-2" data-translate="username">ชื่อผู้ใช้</label>
                            <input type="text" id="registerUsername" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent" placeholder="กรอกชื่อผู้ใช้ (อย่างน้อย 3 ตัวอักษร)">
                        </div>
                        
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-2" data-translate="password">รหัสผ่าน</label>
                            <input type="password" id="registerPassword" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent" placeholder="กรอกรหัสผ่าน (อย่างน้อย 4 ตัวอักษร)">
                        </div>
                        
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-2" data-translate="confirmPassword">ยืนยันรหัสผ่าน</label>
                            <input type="password" id="confirmPassword" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent" placeholder="ยืนยันรหัสผ่าน">
                        </div>
                        
                        <button type="submit" class="w-full bg-green-600 hover:bg-green-700 text-white font-semibold py-3 px-6 rounded-lg transition duration-200" data-translate="registerBtn">
                            สมัครสมาชิก
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <!-- Main App -->
    <div id="mainApp" class="hidden min-h-screen">
        <!-- Navigation -->
        <nav class="bg-white shadow-lg">
            <div class="max-w-7xl mx-auto px-4">
                <div class="flex justify-between items-center py-4">
                    <div class="flex items-center space-x-4">
                        <h1 class="text-2xl font-bold text-gray-800">🏃‍♂️ FitTracker Thailand</h1>
                        <span id="welcomeUser" class="text-gray-600"></span>
                    </div>
                    
                    <div class="flex space-x-4">
                        <button id="runningTab" class="px-4 py-2 bg-blue-600 text-white rounded-lg font-medium" data-translate="running">การวิ่ง</button>
                        <button id="gymTab" class="px-4 py-2 bg-gray-200 text-gray-700 rounded-lg font-medium hover:bg-gray-300" data-translate="gym">เวท/คาร์ดิโอ</button>
                        <button id="statsTab" class="px-4 py-2 bg-gray-200 text-gray-700 rounded-lg font-medium hover:bg-gray-300" data-translate="stats">กราฟสถิติ</button>
                        <button id="leaderboardTab" class="px-4 py-2 bg-gray-200 text-gray-700 rounded-lg font-medium hover:bg-gray-300" data-translate="leaderboard">จัดอันดับ</button>
                        <button id="logoutBtn" class="px-4 py-2 bg-red-500 text-white rounded-lg font-medium hover:bg-red-600" data-translate="logout">ออกจากระบบ</button>
                    </div>
                </div>
            </div>
        </nav>

        <!-- Running Calculator -->
        <div id="runningSection" class="max-w-7xl mx-auto p-6">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                <!-- Calculator -->
                <div class="bg-white rounded-2xl card-shadow p-6">
                    <h2 class="text-2xl font-bold text-gray-800 mb-6">🏃‍♂️ คำนวณแคลอรี่การวิ่ง</h2>
                    
                    <form id="runningForm" class="space-y-6">
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-2" data-translate="weight">น้ำหนัก (กิโลกรัม)</label>
                            <input type="number" id="weight" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500" placeholder="เช่น 70">
                        </div>
                        
                        <div class="relative">
                            <label class="block text-sm font-medium text-gray-700 mb-2" data-translate="province">จังหวัด</label>
                            <input type="text" id="provinceInput" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500" placeholder="พิมพ์ชื่อจังหวัด..." autocomplete="off">
                            <div id="provinceDropdown" class="autocomplete-dropdown hidden"></div>
                            <input type="hidden" id="selectedProvince">
                        </div>
                        
                        <div class="relative">
                            <label class="block text-sm font-medium text-gray-700 mb-2" data-translate="location">สถานที่วิ่ง (ไม่บังคับ)</label>
                            <input type="text" id="locationInput" disabled class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100" placeholder="เลือกจังหวัดก่อน..." autocomplete="off">
                            <div id="locationDropdown" class="autocomplete-dropdown hidden"></div>
                            <input type="hidden" id="selectedLocation">
                        </div>
                        
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-2" data-translate="distance">ระยะทาง</label>
                            <div class="flex space-x-2">
                                <input type="number" id="distance" step="0.1" required class="flex-1 px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500" placeholder="เช่น 3.1">
                                <select id="distanceUnit" class="px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500">
                                    <option value="km" data-translate="km">กิโลเมตร</option>
                                    <option value="m" data-translate="m">เมตร</option>
                                </select>
                            </div>
                        </div>
                        
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-2" data-translate="speed">ระดับความเร็ว</label>
                            <select id="runningSpeed" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500">
                                <option value="" data-translate="selectSpeed">เลือกระดับความเร็ว</option>
                                <option value="slow" data-translate="slow">เดินเร็ว/วิ่งช้า (5-6 กม./ชม.)</option>
                                <option value="moderate" data-translate="moderate">วิ่งปานกลาง (7-8 กม./ชม.)</option>
                                <option value="fast" data-translate="fast">วิ่งเร็ว (9-10 กม./ชม.)</option>
                                <option value="very_fast" data-translate="very_fast">วิ่งเร็วมาก (11+ กม./ชม.)</option>
                            </select>
                        </div>
                        
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-2" data-translate="rounds">จำนวนรอบ</label>
                            <input type="number" id="rounds" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500" placeholder="เช่น 2" value="1">
                        </div>
                        
                        <button type="submit" class="w-full bg-green-600 hover:bg-green-700 text-white font-semibold py-3 px-6 rounded-lg transition duration-200" data-translate="calculate">
                            คำนวณแคลอรี่
                        </button>
                    </form>
                    
                    <div id="runningResult" class="hidden mt-6 p-4 bg-green-50 border border-green-200 rounded-lg">
                        <h3 class="font-semibold text-green-800 mb-2">ผลการคำนวณ</h3>
                        <div id="runningCalories" class="text-2xl font-bold text-green-600"></div>
                        <div id="runningDetails" class="text-sm text-green-700 mt-2"></div>
                    </div>
                </div>
                
                <!-- Weekly Stats -->
                <div class="bg-white rounded-2xl card-shadow p-6">
                    <h2 class="text-2xl font-bold text-gray-800 mb-6">📊 สถิติสัปดาห์นี้</h2>
                    
                    <div class="space-y-4">
                        <div class="flex justify-between items-center p-4 bg-blue-50 rounded-lg">
                            <span class="font-medium text-blue-800">แคลอรี่รวม</span>
                            <span id="weeklyCalories" class="text-2xl font-bold text-blue-600">0 kcal</span>
                        </div>
                        
                        <div class="flex justify-between items-center p-4 bg-purple-50 rounded-lg">
                            <span class="font-medium text-purple-800">ระยะทางรวม</span>
                            <span id="weeklyDistance" class="text-2xl font-bold text-purple-600">0 km</span>
                        </div>
                        
                        <div class="flex justify-between items-center p-4 bg-orange-50 rounded-lg">
                            <span class="font-medium text-orange-800">อันดับในจังหวัด</span>
                            <span id="provinceRank" class="text-2xl font-bold text-orange-600">-</span>
                        </div>
                        
                        <div class="flex justify-between items-center p-4 bg-red-50 rounded-lg">
                            <span class="font-medium text-red-800">อันดับประเทศ</span>
                            <span id="nationalRank" class="text-2xl font-bold text-red-600">-</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Gym/Cardio Calculator -->
        <div id="gymSection" class="hidden max-w-7xl mx-auto p-6">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                <!-- Calculator -->
                <div class="bg-white rounded-2xl card-shadow p-6">
                    <h2 class="text-2xl font-bold text-gray-800 mb-6">💪 คำนวณแคลอรี่เวท/คาร์ดิโอ</h2>
                    
                    <form id="gymForm" class="space-y-6">
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-2">น้ำหนัก (กิโลกรัม)</label>
                            <input type="number" id="gymWeight" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500" placeholder="เช่น 70">
                        </div>
                        
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-2">ประเภทการออกกำลังกาย</label>
                            <select id="exerciseType" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500">
                                <option value="">เลือกประเภท</option>
                                <option value="pushup">ดันพื้น (Push-ups)</option>
                                <option value="situp">ซิทอัพ (Sit-ups)</option>
                                <option value="squat">สควอท (Squats)</option>
                                <option value="pullup">ดึงข้อ (Pull-ups)</option>
                                <option value="plank">แพลงค์ (Plank)</option>
                                <option value="burpee">เบอร์ปี้ (Burpees)</option>
                                <option value="jumpingjack">กระโดดกบ (Jumping Jacks)</option>
                            </select>
                        </div>
                        
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-2">จำนวนครั้ง/นาที</label>
                            <input type="number" id="reps" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500" placeholder="เช่น 15">
                        </div>
                        
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-2">จำนวนเซ็ต</label>
                            <input type="number" id="sets" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500" placeholder="เช่น 3" value="1">
                        </div>
                        
                        <button type="submit" class="w-full bg-purple-600 hover:bg-purple-700 text-white font-semibold py-3 px-6 rounded-lg transition duration-200">
                            คำนวณแคลอรี่
                        </button>
                    </form>
                    
                    <div id="gymResult" class="hidden mt-6 p-4 bg-purple-50 border border-purple-200 rounded-lg">
                        <h3 class="font-semibold text-purple-800 mb-2">ผลการคำนวณ</h3>
                        <div id="gymCalories" class="text-2xl font-bold text-purple-600"></div>
                        <div id="gymDetails" class="text-sm text-purple-700 mt-2"></div>
                    </div>
                </div>
                
                <!-- Gym Weekly Stats -->
                <div class="bg-white rounded-2xl card-shadow p-6">
                    <h2 class="text-2xl font-bold text-gray-800 mb-6">📊 สถิติเวท/คาร์ดิโอ</h2>
                    
                    <div class="space-y-4">
                        <div class="flex justify-between items-center p-4 bg-purple-50 rounded-lg">
                            <span class="font-medium text-purple-800">แคลอรี่รวม</span>
                            <span id="weeklyGymCalories" class="text-2xl font-bold text-purple-600">0 kcal</span>
                        </div>
                        
                        <div class="flex justify-between items-center p-4 bg-indigo-50 rounded-lg">
                            <span class="font-medium text-indigo-800">เซ็ตรวม</span>
                            <span id="weeklySets" class="text-2xl font-bold text-indigo-600">0 sets</span>
                        </div>
                        
                        <div class="flex justify-between items-center p-4 bg-pink-50 rounded-lg">
                            <span class="font-medium text-pink-800">อันดับเวท/คาร์ดิโอ</span>
                            <span id="gymRank" class="text-2xl font-bold text-pink-600">-</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Statistics Charts -->
        <div id="statsSection" class="hidden max-w-7xl mx-auto p-6">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                <!-- Weekly Calories Chart -->
                <div class="bg-white rounded-2xl card-shadow p-6">
                    <h2 class="text-2xl font-bold text-gray-800 mb-6">📊 แคลอรี่รายสัปดาห์</h2>
                    <div class="chart-container">
                        <canvas id="weeklyCaloriesChart"></canvas>
                    </div>
                </div>
                
                <!-- Exercise Distribution -->
                <div class="bg-white rounded-2xl card-shadow p-6">
                    <h2 class="text-2xl font-bold text-gray-800 mb-6">🥧 สัดส่วนการออกกำลังกาย</h2>
                    <div class="chart-container">
                        <canvas id="exerciseDistributionChart"></canvas>
                    </div>
                </div>
                
                <!-- Daily Progress -->
                <div class="bg-white rounded-2xl card-shadow p-6">
                    <h2 class="text-2xl font-bold text-gray-800 mb-6">📈 ความก้าวหน้ารายวัน</h2>
                    <div class="chart-container">
                        <canvas id="dailyProgressChart"></canvas>
                    </div>
                </div>
                
                <!-- Province Comparison -->
                <div class="bg-white rounded-2xl card-shadow p-6">
                    <h2 class="text-2xl font-bold text-gray-800 mb-6">🗺️ เปรียบเทียบจังหวัด</h2>
                    <div class="chart-container">
                        <canvas id="provinceComparisonChart"></canvas>
                    </div>
                </div>
            </div>
        </div>

        <!-- Leaderboard -->
        <div id="leaderboardSection" class="hidden max-w-7xl mx-auto p-6">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                <!-- Running Leaderboard -->
                <div class="bg-white rounded-2xl card-shadow p-6">
                    <h2 class="text-2xl font-bold text-gray-800 mb-6">🏆 อันดับการวิ่ง</h2>
                    
                    <div class="mb-4">
                        <select id="leaderboardFilter" class="px-4 py-2 border border-gray-300 rounded-lg">
                            <option value="national">ระดับประเทศ</option>
                            <option value="province">ระดับจังหวัด</option>
                        </select>
                    </div>
                    
                    <div class="overflow-x-auto">
                        <table class="w-full">
                            <thead>
                                <tr class="border-b border-gray-200">
                                    <th class="text-left py-3 px-2">อันดับ</th>
                                    <th class="text-left py-3 px-2">ชื่อ</th>
                                    <th class="text-left py-3 px-2">แคลอรี่</th>
                                    <th class="text-left py-3 px-2">ระยะทาง</th>
                                </tr>
                            </thead>
                            <tbody id="runningLeaderboard">
                                <!-- Dynamic content -->
                            </tbody>
                        </table>
                    </div>
                </div>
                
                <!-- Gym Leaderboard -->
                <div class="bg-white rounded-2xl card-shadow p-6">
                    <h2 class="text-2xl font-bold text-gray-800 mb-6">💪 อันดับเวท/คาร์ดิโอ</h2>
                    
                    <div class="overflow-x-auto">
                        <table class="w-full">
                            <thead>
                                <tr class="border-b border-gray-200">
                                    <th class="text-left py-3 px-2">อันดับ</th>
                                    <th class="text-left py-3 px-2">ชื่อ</th>
                                    <th class="text-left py-3 px-2">แคลอรี่</th>
                                    <th class="text-left py-3 px-2">เซ็ต</th>
                                </tr>
                            </thead>
                            <tbody id="gymLeaderboard">
                                <!-- Dynamic content -->
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Data Storage
        let currentUser = null;
        let users = JSON.parse(localStorage.getItem('fitTrackerUsers')) || {};
        let runningData = JSON.parse(localStorage.getItem('runningData')) || [];
        let gymData = JSON.parse(localStorage.getItem('gymData')) || [];
        let currentLanguage = localStorage.getItem('fitTrackerLanguage') || 'th';
        let customLocations = JSON.parse(localStorage.getItem('customLocations')) || {};
        
        // Chart instances
        let weeklyCaloriesChart = null;
        let exerciseDistributionChart = null;
        let dailyProgressChart = null;
        let provinceComparisonChart = null;

        // Speed multipliers for calorie calculation
        const speedMultipliers = {
            'slow': 0.8,      // เดินเร็ว/วิ่งช้า
            'moderate': 1.0,  // วิ่งปานกลาง (base)
            'fast': 1.3,      // วิ่งเร็ว
            'very_fast': 1.6  // วิ่งเร็วมาก
        };

        // Exercise calorie rates (calories per rep per kg) - ปรับให้สมจริงขึ้น
        const exerciseRates = {
            'pushup': 0.05,     // ดันพื้น 1 ครั้ง ≈ 3.5 แคลอรี่ (70 กก.)
            'situp': 0.04,      // ซิทอัพ 1 ครั้ง ≈ 2.8 แคลอรี่ (70 กก.)
            'squat': 0.06,      // สควอท 1 ครั้ง ≈ 4.2 แคลอรี่ (70 กก.)
            'pullup': 0.12,     // ดึงข้อ 1 ครั้ง ≈ 8.4 แคลอรี่ (70 กก.) - หนักกว่า
            'plank': 0.8,       // แพลงค์ต่อนาที ≈ 56 แคลอรี่ (70 กก.)
            'burpee': 0.15,     // เบอร์ปี้ 1 ครั้ง ≈ 10.5 แคลอรี่ (70 กก.) - เผาผลาญสูง
            'jumpingjack': 0.03 // กระโดดกบ 1 ครั้ง ≈ 2.1 แคลอรี่ (70 กก.)
        };

        // Language translations
        const translations = {
            th: {
                appTitle: '🏃‍♂️ FitTracker Thailand',
                appSubtitle: 'ระบบคำนวณแคลอรี่การออกกำลังกาย',
                login: 'เข้าสู่ระบบ',
                register: 'สมัครสมาชิก',
                username: 'ชื่อผู้ใช้',
                password: 'รหัสผ่าน',
                confirmPassword: 'ยืนยันรหัสผ่าน',
                loginBtn: 'เข้าสู่ระบบ',
                registerBtn: 'สมัครสมาชิก',
                demoText: 'ทดลองใช้: username: demo, password: 1234',
                running: 'การวิ่ง',
                gym: 'เวท/คาร์ดิโอ',
                stats: 'กราฟสถิติ',
                leaderboard: 'จัดอันดับ',
                logout: 'ออกจากระบบ',
                weight: 'น้ำหนัก (กิโลกรัม)',
                province: 'จังหวัด',
                location: 'สถานที่วิ่ง (ไม่บังคับ)',
                distance: 'ระยะทาง',
                speed: 'ระดับความเร็ว',
                rounds: 'จำนวนรอบ',
                calculate: 'คำนวณแคลอรี่',
                km: 'กิโลเมตร',
                m: 'เมตร',
                slow: 'เดินเร็ว/วิ่งช้า (5-6 กม./ชม.)',
                moderate: 'วิ่งปานกลาง (7-8 กม./ชม.)',
                fast: 'วิ่งเร็ว (9-10 กม./ชม.)',
                very_fast: 'วิ่งเร็วมาก (11+ กม./ชม.)',
                selectSpeed: 'เลือกระดับความเร็ว'
            },
            en: {
                appTitle: '🏃‍♂️ FitTracker Thailand',
                appSubtitle: 'Exercise Calorie Calculator System',
                login: 'Login',
                register: 'Register',
                username: 'Username',
                password: 'Password',
                confirmPassword: 'Confirm Password',
                loginBtn: 'Login',
                registerBtn: 'Register',
                demoText: 'Demo: username: demo, password: 1234',
                running: 'Running',
                gym: 'Gym/Cardio',
                stats: 'Statistics',
                leaderboard: 'Leaderboard',
                logout: 'Logout',
                weight: 'Weight (kg)',
                province: 'Province',
                location: 'Running Location (Optional)',
                distance: 'Distance',
                speed: 'Speed Level',
                rounds: 'Rounds',
                calculate: 'Calculate Calories',
                km: 'Kilometers',
                m: 'Meters',
                slow: 'Fast Walk/Slow Run (5-6 km/h)',
                moderate: 'Moderate Run (7-8 km/h)',
                fast: 'Fast Run (9-10 km/h)',
                very_fast: 'Very Fast Run (11+ km/h)',
                selectSpeed: 'Select Speed Level'
            }
        };

        // Province and Location Data (77 provinces complete)
        const provinceData = {
            'กรุงเทพมหานคร': ['สวนลุมพินี', 'สวนจตุจักร', 'สวนเบญจกิติ', 'สวนรถไฟ', 'สวนสราญรมย์'],
            'กระบี่': ['หาดอ่าวนาง', 'เกาะพีพี', 'ถ้ำเสือ', 'หาดไร่เลย์', 'เกาะปอดะ'],
            'กาญจนบุรี': ['สะพานข้ามแม่น้ำแคว', 'อุทยานแห่งชาติเอราวัณ', 'ถ้ำเซเว่น', 'วัดถ้ำเสือ', 'เขื่อนศรีนครินทร์'],
            'กาฬสินธุ์': ['พระธาตุยาคู', 'ลำน้ำชี', 'สวนสาธารณะกาฬสินธุ์', 'วัดกลางมิ่งเมือง', 'ตลาดเก่ากาฬสินธุ์'],
            'กำแพงเพชร': ['พระราชวังจักรีมหาปราสาท', 'อุทยานประวัติศาสตร์กำแพงเพชร', 'วัดพระธาตุ', 'ตลาดเก่า', 'สวนสาธารณะ'],
            'ขอนแก่น': ['มหาวิทยาลัยขอนแก่น', 'บึงแก่นนคร', 'ถนนศรีจันทร์', 'สวนสาธารณะขอนแก่น', 'ตลาดต้นตาล'],
            'จันทบุรี': ['ตลาดน้ำคลองสวน', 'เกาะช้าง', 'น้ำตกพลิ้ว', 'อุทยานแห่งชาติเขาคิชฌกูฏ', 'หาดแหลมสิงห์'],
            'ฉะเชิงเทรา': ['วัดโสธรวรารามวรวิหาร', 'ตลาดน้ำบางน้ำผึ้ง', 'สวนสาธารณะ', 'ถนนเก่า', 'วัดปากน้ำ'],
            'ชลบุรี': ['หาดพัทยา', 'เกาะล้าน', 'สวนนงนุช', 'ตลาดน้ำสี่ภาค', 'วัดยานสังวรารามวรมหาวิหาร'],
            'ชัยนาท': ['อุทยานนกน้ำชัยนาท', 'วัดพระบรมธาตุชัยนาท', 'ตลาดเก่า', 'สวนสาธารณะ', 'แม่น้ำเจ้าพระยา'],
            'ชัยภูมิ': ['ปราสาทหินเผาไผ่', 'อุทยานแห่งชาติป่าหินงาม', 'ภูลังกา', 'วัดธาตุ', 'ตลาดเก่าชัยภูมิ'],
            'ชุมพร': ['หาดทุ่งวัวแล', 'เกาะเต่า', 'อุทยานแห่งชาติหมู่เกาะชุมพร', 'วัดพระบรมธาตุ', 'ตลาดเก่า'],
            'เชียงราย': ['วัดร่องขุ่น', 'สามเหลี่ยมทองคำ', 'ดอยตุง', 'หอนาฬิกาเชียงราย', 'วัดพระแก้ว'],
            'เชียงใหม่': ['สวนสวนดอก', 'มหาวิทยาลัยเชียงใหม่', 'ถนนคนเดิน', 'ดอยสุเทพ', 'วัดเจดีย์หลวง'],
            'ตรัง': ['หาดปากเมง', 'เกาะมุก', 'ถ้ำเลเซ', 'อุทยานแห่งชาติหาดเจ้าไหม', 'ตลาดเก่าตรัง'],
            'ตราด': ['เกาะช้าง', 'เกาะกูด', 'หาดไก่แบ้', 'อุทยานแห่งชาติหมู่เกาะช้าง', 'ตลาดเก่าตราด'],
            'ตาก': ['อุทยานแห่งชาติตากสินมหาราช', 'สะพานมอญ', 'วัดพระบรมธาตุ', 'ตลาดเก่า', 'แม่น้ำปิง'],
            'นครนายก': ['น้ำตกนางรอง', 'วัดพระพุทธบาทตากผ้า', 'สวนผึ้ง', 'ตลาดเก่า', 'แม่น้ำนครนายก'],
            'นครปฐม': ['พระปฐมเจดีย์', 'สวนผึ้ง', 'ตลาดดอนหวาย', 'มหาวิทยาลัยศิลปกรรม', 'วัดไร่ขิง'],
            'นครพนม': ['พระธาตุพนม', 'แม่น้ำโขง', 'ตลาดอินโดจีน', 'วัดมหาธาตุ', 'สวนสาธารณะ'],
            'นครราชสีมา': ['มหาวิทยาลัยเทคโนโลยีสุรนารี', 'เขาใหญ่', 'ปราสาทหินพิมาย', 'สวนสาธารณะสวนใหม่', 'ถนนยะโม'],
            'นครศรีธรรมราช': ['วัดพระมหาธาตุ', 'เขาหลวง', 'หาดคีรีวง', 'ตลาดเก่านครศรีธรรมราช', 'ถนนราชดำเนิน'],
            'นครสวรรค์': ['บึงบอระเพ็ด', 'วัดพระบรมธาตุ', 'ตลาดเก่า', 'สวนสาธารณะ', 'แม่น้ำน่าน'],
            'นนทบุรี': ['เกาะเกร็ด', 'วัดชลประทานรังสฤษดิ์', 'สวนสาธารณะนนทบุรี', 'ถนนติวานนท์', 'ตลาดเก่า'],
            'นราธิวาส': ['หาดนราธิวาส', 'วัดเขาคง', 'ตลาดเก่า', 'สวนสาธารณะ', 'ถนนภูเก็ต-นราธิวาส'],
            'น่าน': ['วัดภูมินทร์', 'แม่น้ำน่าน', 'ตลาดเก่า', 'สวนสาธารณะ', 'ถนนสุมนเทวราช'],
            'บึงกาฬ': ['หนองหาน', 'วัดพระธาตุ', 'ตลาดเก่า', 'สวนสาธารณะ', 'แม่น้ำโขง'],
            'บุรีรัมย์': ['ปราสาทเขาพนมรุ้ง', 'สนามช้างอารีนา', 'วัดพระธาตุ', 'ตลาดเก่า', 'สวนสาธารณะ'],
            'ปทุมธานี': ['มหาวิทยาลัยธรรมศาสตร์', 'ตลาดน้ำคลองลาดมะยม', 'สวนสาธารณะปทุมธานี', 'ถนนรังสิต-นครนายก', 'วัดพระธรรมกาย'],
            'ประจวบคีรีขันธ์': ['หาดหัวหิน', 'เขาสามร้อยยอด', 'วัดพระธาตุ', 'ตลาดเก่า', 'สวนสาธารณะ'],
            'ปราจีนบุรี': ['วัดไผ่โรงวัว', 'เขาใหญ่', 'ตลาดเก่า', 'สวนสาธารณะ', 'แม่น้ำบางปะกง'],
            'ปัตตานี': ['มัสยิดกรือเซะ', 'หาดปัตตานี', 'ตลาดเก่า', 'สวนสาธารณะ', 'วัดพระธาตุ'],
            'พระนครศรีอยุธยา': ['วัดพระศรีสรรเพชญ์', 'วัดมหาธาตุ', 'ตลาดน้ำอยุธยา', 'สวนสาธารณะ', 'แม่น้ำเจ้าพระยา'],
            'พังงา': ['อ่าวพังงา', 'เกาะเจมส์บอนด์', 'ถ้ำพุงช้าง', 'หาดนางทอง', 'ตลาดเก่า'],
            'พัทลุง': ['ทะเลสาบสงขลา', 'เขาอก', 'วัดพระธาตุ', 'ตลาดเก่า', 'สวนสาธารณะ'],
            'พิจิตร': ['วัดพระศรีรัตนมหาธาตุ', 'บึงสีไฟ', 'ตลาดเก่า', 'สวนสาธารณะ', 'แม่น้ำน่าน'],
            'พิษณุโลก': ['วัดพระศรีรัตนมหาธาตุ', 'อุทยานประวัติศาสตร์สุโขทัย', 'ตลาดเก่า', 'สวนสาธารณะ', 'แม่น้ำน่าน'],
            'เพชรบุรี': ['พระนครคีรี', 'หาดชะอำ', 'วัดไผ่ร่องวัว', 'ตลาดเก่า', 'สวนสาธารณะ'],
            'เพชรบูรณ์': ['เขาค้อ', 'วิทยาลัยป่าไผ่', 'วัดพระธาตุ', 'ตลาดเก่า', 'สวนสาธารณะ'],
            'แพร่': ['วัดพระธาตุช่อแฮ', 'แม่น้ำยม', 'ตลาดเก่า', 'สวนสาธารณะ', 'ถนนเจริญเมือง'],
            'ภูเก็ต': ['หาดป่าตอง', 'หาดกะตะ', 'หาดกะรน', 'เมืองเก่าภูเก็ต', 'วัดฉลอง'],
            'มหาสารคาม': ['มหาวิทยาลัยมหาสารคาม', 'วัดพระธาตุนาดูน', 'ตลาดเก่า', 'สวนสาธารณะ', 'บึงพลาญชัย'],
            'มุกดาหาร': ['หินสามพัน', 'แม่น้ำโขง', 'วัดพระธาตุ', 'ตลาดอินโดจีน', 'สวนสาธารณะ'],
            'แม่ฮ่องสอน': ['ปางอุ๋ง', 'วัดพระธาตุดอยกองมู', 'ตลาดเก่า', 'สวนสาธารณะ', 'ถนนคนเดิน'],
            'ยโซธร': ['วัดพระธาตุอานันท์', 'ประตูน้ำ', 'ตลาดเก่า', 'สวนสาธารณะ', 'แม่น้ำชี'],
            'ยะลา': ['วัดพระธาตุเจดีย์', 'หาดยะลา', 'ตลาดเก่า', 'สวนสาธารณะ', 'ถนนสิรินธร'],
            'ร้อยเอ็ด': ['วัดพระมหาธาตุ', 'บึงพลาญชัย', 'ตลาดเก่า', 'สวนสาธารณะ', 'ถนนเพชรเกษม'],
            'ระนอง': ['น้ำพุร้อนระนอง', 'เกาะช้าง', 'วัดพระธาตุ', 'ตลาดเก่า', 'สวนสาธารณะ'],
            'ระยอง': ['หาดแม่รำพึง', 'เกาะเสม็ด', 'สวนสาธารณะระยอง', 'ถนนสุขุมวิท', 'วัดป่าประดู่'],
            'ราชบุรี': ['ตลาดน้ำดำเนินสะดวก', 'เขาบิน', 'วัดพระธาตุ', 'ตลาดเก่า', 'แม่น้ำแม่กลอง'],
            'ลพบุรี': ['วัดพระศรีรัตนมหาธาตุ', 'ปราสาทนารายณ์ราชนิเวศน์', 'ตลาดเก่า', 'สวนสาธารณะ', 'ถนนนาไผ่'],
            'ลำปาง': ['วัดพระธาตุลำปางหลวง', 'ตลาดกาดกองต้า', 'สวนสาธารณะ', 'ถนนตลาดเก้า', 'แม่น้ำวัง'],
            'ลำพูน': ['วัดพระธาตุหริภุญชัย', 'ตลาดเก่า', 'สวนสาธารณะ', 'ถนนอินทวโรรส', 'แม่น้ำกวง'],
            'เลย': ['ภูกระดึง', 'วัดพระธาตุ', 'ตลาดเก่า', 'สวนสาธารณะ', 'แม่น้ำโขง'],
            'ศรีสะเกษ': ['ปราสาทสระกำแพงใหญ่', 'วัดพระธาตุ', 'ตลาดเก่า', 'สวนสาธารณะ', 'แม่น้ำมูล'],
            'สกลนคร': ['พระธาตุเชิงชุม', 'หนองหาน', 'ตลาดเก่า', 'สวนสาธารณะ', 'แม่น้ำโขง'],
            'สงขลา': ['มหาวิทยาลัยสงขลานครินทร์', 'หาดสมิหลา', 'ทะเลสาบสงขลา', 'เกาะยอ', 'ตลาดเก่า'],
            'สตูล': ['เกาะตะรุเตา', 'เกาะอาดัง', 'วัดพระธาตุ', 'ตลาดเก่า', 'สวนสาธารณะ'],
            'สมุทรปราการ': ['เมืองโบราณ', 'วัดอโศการาม', 'ตลาดน้ำบางน้ำผึ้ง', 'สนามบินสุวรรณภูมิ', 'วัดบางพลี'],
            'สมุทรสงคราม': ['ตลาดน้ำอัมพวา', 'วัดบางกุ้ง', 'สวนสาธารณะ', 'ถนนเพชรเกษม', 'แม่น้ำแม่กลอง'],
            'สมุทรสาคร': ['วัดพระสมุทรเจดีย์', 'ตลาดเก่า', 'สวนสาธารณะ', 'ถนนเพชรเกษม', 'แม่น้ำท่าจีน'],
            'สระแก้ว': ['อรัญประเทศ', 'วัดพระธาตุ', 'ตลาดเก่า', 'สวนสาธารณะ', 'ถนนสุวรรณศร'],
            'สระบุรี': ['วัดพระพุทธบาทราชวรมหาวิหาร', 'เขาสามหลัน', 'ตลาดเก่า', 'สวนสาธารณะ', 'ถนนมิตรภาพ'],
            'สิงห์บุรี': ['วัดพระศรีรัตนมหาธาตุ', 'แม่น้ำเจ้าพระยา', 'ตลาดเก่า', 'สวนสาธารณะ', 'ถนนบางปะหัน'],
            'สุโขทัย': ['อุทยานประวัติศาสตร์สุโขทัย', 'วัดมหาธาตุ', 'ตลาดเก่า', 'สวนสาธารณะ', 'แม่น้ำยม'],
            'สุพรรณบุรี': ['หอพระอิศวรเทพ', 'วัดพระศรีรัตนมหาธาตุ', 'ตลาดเก่า', 'สวนสาธารณะ', 'แม่น้ำท่าจีน'],
            'สุราษฎร์ธานี': ['เกาะสมุย', 'เกาะพะงัน', 'เกาะเต่า', 'อุทยานแห่งชาติเขาสก', 'ตลาดเก่า'],
            'สุรินทร์': ['ปราสาทตาเมือน', 'งานช้างสุรินทร์', 'วัดพระธาตุ', 'ตลาดเก่า', 'สวนสาธารณะ'],
            'หนองคาย': ['ศาลาแก้วกู่', 'แม่น้ำโขง', 'วัดพระธาตุ', 'ตลาดอินโดจีน', 'สวนสาธารณะ'],
            'หนองบัวลำภู': ['วัดพระธาตุ', 'เขาค้อ', 'ตลาดเก่า', 'สวนสาธารณะ', 'แม่น้ำโขง'],
            'อ่างทอง': ['วัดพระศรีรัตนมหาธาตุ', 'แม่น้ำเจ้าพระยา', 'ตลาดเก่า', 'สวนสาธารณะ', 'ถนนบางปะอิน'],
            'อำนาจเจริญ': ['วัดพระธาตุ', 'แม่น้ำโขง', 'ตลาดเก่า', 'สวนสาธารณะ', 'ถนนมิตรภาพ'],
            'อุดรธานี': ['หนองประจักษ์', 'บ้านเชียง', 'ภูพระบาท', 'ตลาดกลางเวียง', 'มหาวิทยาลัยอุดรธานี'],
            'อุตรดิตถ์': ['วัดพระบรมธาตุ', 'แม่น้ำน่าน', 'ตลาดเก่า', 'สวนสาธารณะ', 'ถนนท่าอิฐ'],
            'อุทัยธานี': ['วัดสังกัสรัตนคีรี', 'หุบกะพง', 'ตลาดเก่า', 'สวนสาธารณะ', 'แม่น้ำสะแกกรัง'],
            'อุบลราชธานี': ['วัดพระธาตุนงบัว', 'แม่น้ำโขง', 'ตลาดเก่า', 'สวนสาธารณะ', 'ถนนอุปราช']
        };

        // Initialize
        document.addEventListener('DOMContentLoaded', function() {
            setupEventListeners();
            setupAutocomplete();
            updateLanguage();
            
            // Add demo user
            if (!users['demo']) {
                users['demo'] = { password: '1234', province: 'กรุงเทพมหานคร' };
                localStorage.setItem('fitTrackerUsers', JSON.stringify(users));
            }
            
            // Add sample data if empty
            if (runningData.length === 0) {
                addSampleData();
            }
        });

        function updateLanguage() {
            document.getElementById('languageSelector').value = currentLanguage;
            const t = translations[currentLanguage];
            
            // Update login screen
            document.getElementById('appTitle').textContent = t.appTitle;
            document.getElementById('appSubtitle').textContent = t.appSubtitle;
            
            // Update form labels and buttons
            document.querySelectorAll('[data-translate]').forEach(element => {
                const key = element.getAttribute('data-translate');
                if (t[key]) {
                    if (element.tagName === 'INPUT' && element.type === 'submit') {
                        element.value = t[key];
                    } else if (element.tagName === 'BUTTON') {
                        element.textContent = t[key];
                    } else if (element.tagName === 'OPTION') {
                        element.textContent = t[key];
                    } else {
                        element.textContent = t[key];
                    }
                }
            });
        }

        function setupEventListeners() {
            // Language selector
            document.getElementById('languageSelector').addEventListener('change', function() {
                currentLanguage = this.value;
                localStorage.setItem('fitTrackerLanguage', currentLanguage);
                updateLanguage();
            });

            // Login and Register
            document.getElementById('loginForm').addEventListener('submit', handleLogin);
            document.getElementById('registerForm').addEventListener('submit', handleRegister);
            document.getElementById('logoutBtn').addEventListener('click', handleLogout);

            // Navigation
            document.getElementById('runningTab').addEventListener('click', () => showSection('running'));
            document.getElementById('gymTab').addEventListener('click', () => showSection('gym'));
            document.getElementById('statsTab').addEventListener('click', () => showSection('stats'));
            document.getElementById('leaderboardTab').addEventListener('click', () => showSection('leaderboard'));

            // Forms
            document.getElementById('runningForm').addEventListener('submit', handleRunningCalculation);
            document.getElementById('gymForm').addEventListener('submit', handleGymCalculation);

            // Leaderboard filter
            document.getElementById('leaderboardFilter').addEventListener('change', updateLeaderboard);
        }

        function setupAutocomplete() {
            const provinceInput = document.getElementById('provinceInput');
            const provinceDropdown = document.getElementById('provinceDropdown');
            const locationInput = document.getElementById('locationInput');
            const locationDropdown = document.getElementById('locationDropdown');
            
            let selectedProvinceIndex = -1;
            let selectedLocationIndex = -1;

            // Province autocomplete
            provinceInput.addEventListener('input', function() {
                const value = this.value.toLowerCase();
                const provinces = Object.keys(provinceData).filter(province => 
                    province.toLowerCase().includes(value)
                );
                
                if (value && provinces.length > 0) {
                    provinceDropdown.innerHTML = '';
                    provinces.forEach((province, index) => {
                        const item = document.createElement('div');
                        item.className = 'autocomplete-item';
                        item.textContent = province;
                        item.addEventListener('click', () => selectProvince(province));
                        provinceDropdown.appendChild(item);
                    });
                    provinceDropdown.classList.remove('hidden');
                    selectedProvinceIndex = -1;
                } else {
                    provinceDropdown.classList.add('hidden');
                }
            });

            provinceInput.addEventListener('keydown', function(e) {
                const items = provinceDropdown.querySelectorAll('.autocomplete-item');
                
                if (e.key === 'ArrowDown') {
                    e.preventDefault();
                    selectedProvinceIndex = Math.min(selectedProvinceIndex + 1, items.length - 1);
                    updateSelection(items, selectedProvinceIndex);
                } else if (e.key === 'ArrowUp') {
                    e.preventDefault();
                    selectedProvinceIndex = Math.max(selectedProvinceIndex - 1, -1);
                    updateSelection(items, selectedProvinceIndex);
                } else if (e.key === 'Enter' && selectedProvinceIndex >= 0) {
                    e.preventDefault();
                    items[selectedProvinceIndex].click();
                } else if (e.key === 'Escape') {
                    provinceDropdown.classList.add('hidden');
                }
            });

            // Location autocomplete
            locationInput.addEventListener('input', function() {
                const selectedProvince = document.getElementById('selectedProvince').value;
                if (!selectedProvince) return;
                
                const value = this.value.toLowerCase();
                
                // Combine default locations with custom locations
                const defaultLocations = provinceData[selectedProvince] || [];
                const customLocs = customLocations[selectedProvince] || [];
                const allLocations = [...defaultLocations, ...customLocs];
                
                const filteredLocations = allLocations.filter(location => 
                    location.toLowerCase().includes(value)
                );
                
                if (value && filteredLocations.length > 0) {
                    locationDropdown.innerHTML = '';
                    filteredLocations.forEach((location, index) => {
                        const item = document.createElement('div');
                        const isCustom = customLocs.includes(location);
                        item.className = isCustom ? 'autocomplete-item custom-location' : 'autocomplete-item';
                        item.textContent = location;
                        if (isCustom) {
                            item.title = 'สถานที่ที่คุณเพิ่มเอง';
                        }
                        item.addEventListener('click', () => selectLocation(location));
                        locationDropdown.appendChild(item);
                    });
                    locationDropdown.classList.remove('hidden');
                    selectedLocationIndex = -1;
                } else {
                    locationDropdown.classList.add('hidden');
                }
            });

            locationInput.addEventListener('keydown', function(e) {
                const items = locationDropdown.querySelectorAll('.autocomplete-item');
                
                if (e.key === 'ArrowDown') {
                    e.preventDefault();
                    selectedLocationIndex = Math.min(selectedLocationIndex + 1, items.length - 1);
                    updateSelection(items, selectedLocationIndex);
                } else if (e.key === 'ArrowUp') {
                    e.preventDefault();
                    selectedLocationIndex = Math.max(selectedLocationIndex - 1, -1);
                    updateSelection(items, selectedLocationIndex);
                } else if (e.key === 'Enter' && selectedLocationIndex >= 0) {
                    e.preventDefault();
                    items[selectedLocationIndex].click();
                } else if (e.key === 'Escape') {
                    locationDropdown.classList.add('hidden');
                }
            });

            // Close dropdowns when clicking outside
            document.addEventListener('click', function(e) {
                if (!provinceInput.contains(e.target) && !provinceDropdown.contains(e.target)) {
                    provinceDropdown.classList.add('hidden');
                }
                if (!locationInput.contains(e.target) && !locationDropdown.contains(e.target)) {
                    locationDropdown.classList.add('hidden');
                }
            });
        }

        function updateSelection(items, selectedIndex) {
            items.forEach((item, index) => {
                if (index === selectedIndex) {
                    item.classList.add('selected');
                } else {
                    item.classList.remove('selected');
                }
            });
        }

        function selectProvince(province) {
            document.getElementById('provinceInput').value = province;
            document.getElementById('selectedProvince').value = province;
            document.getElementById('provinceDropdown').classList.add('hidden');
            
            // Enable location input
            const locationInput = document.getElementById('locationInput');
            locationInput.disabled = false;
            locationInput.placeholder = 'พิมพ์ชื่อสถานที่... (เช่น มจพ.ปราจีน หรือไม่ใส่ก็ได้)';
            locationInput.value = '';
            document.getElementById('selectedLocation').value = '';
        }

        function selectLocation(location) {
            document.getElementById('locationInput').value = location;
            document.getElementById('selectedLocation').value = location;
            document.getElementById('locationDropdown').classList.add('hidden');
        }

        function saveCustomLocation(province, location) {
            if (!location || !province) return;
            
            // Initialize province array if not exists
            if (!customLocations[province]) {
                customLocations[province] = [];
            }
            
            // Check if location already exists (in both default and custom)
            const defaultLocations = provinceData[province] || [];
            const existingCustom = customLocations[province];
            
            if (!defaultLocations.includes(location) && !existingCustom.includes(location)) {
                customLocations[province].push(location);
                localStorage.setItem('customLocations', JSON.stringify(customLocations));
            }
        }

        function handleLogin(e) {
            e.preventDefault();
            const username = document.getElementById('loginUsername').value.trim();
            const password = document.getElementById('loginPassword').value.trim();

            if (!username || !password) {
                alert('กรุณากรอกชื่อผู้ใช้และรหัสผ่าน');
                return;
            }

            if (users[username] && users[username].password === password) {
                currentUser = username;
                document.getElementById('welcomeUser').textContent = `สวัสดี ${username}`;
                document.getElementById('loginScreen').classList.add('hidden');
                document.getElementById('mainApp').classList.remove('hidden');
                updateUserStats();
            } else {
                alert('ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง');
            }
        }

        function handleRegister(e) {
            e.preventDefault();
            const username = document.getElementById('registerUsername').value.trim();
            const password = document.getElementById('registerPassword').value.trim();
            const confirmPassword = document.getElementById('confirmPassword').value.trim();

            if (!username || !password || !confirmPassword) {
                alert('กรุณากรอกข้อมูลให้ครบถ้วน');
                return;
            }

            if (username.length < 3) {
                alert('ชื่อผู้ใช้ต้องมีอย่างน้อย 3 ตัวอักษร');
                return;
            }

            if (password.length < 4) {
                alert('รหัสผ่านต้องมีอย่างน้อย 4 ตัวอักษร');
                return;
            }

            if (password !== confirmPassword) {
                alert('รหัสผ่านไม่ตรงกัน');
                return;
            }

            if (users[username]) {
                alert('ชื่อผู้ใช้นี้มีอยู่แล้ว กรุณาเลือกชื่อใหม่');
            } else {
                users[username] = { password: password, province: '' };
                localStorage.setItem('fitTrackerUsers', JSON.stringify(users));
                alert('สมัครสมาชิกสำเร็จ! กรุณาเข้าสู่ระบบ');
                
                // Clear register form
                document.getElementById('registerUsername').value = '';
                document.getElementById('registerPassword').value = '';
                document.getElementById('confirmPassword').value = '';
                
                // Fill login form
                document.getElementById('loginUsername').value = username;
                document.getElementById('loginPassword').value = password;
            }
        }

        function handleLogout() {
            currentUser = null;
            document.getElementById('loginScreen').classList.remove('hidden');
            document.getElementById('mainApp').classList.add('hidden');
            
            // Clear all forms
            document.getElementById('loginUsername').value = '';
            document.getElementById('loginPassword').value = '';
            document.getElementById('registerUsername').value = '';
            document.getElementById('registerPassword').value = '';
            document.getElementById('confirmPassword').value = '';
        }

        function showSection(section) {
            // Hide all sections
            document.getElementById('runningSection').classList.add('hidden');
            document.getElementById('gymSection').classList.add('hidden');
            document.getElementById('statsSection').classList.add('hidden');
            document.getElementById('leaderboardSection').classList.add('hidden');

            // Reset tab styles
            document.querySelectorAll('nav button').forEach(btn => {
                if (btn.id !== 'logoutBtn') {
                    btn.className = 'px-4 py-2 bg-gray-200 text-gray-700 rounded-lg font-medium hover:bg-gray-300';
                }
            });

            // Show selected section and highlight tab
            if (section === 'running') {
                document.getElementById('runningSection').classList.remove('hidden');
                document.getElementById('runningTab').className = 'px-4 py-2 bg-blue-600 text-white rounded-lg font-medium';
            } else if (section === 'gym') {
                document.getElementById('gymSection').classList.remove('hidden');
                document.getElementById('gymTab').className = 'px-4 py-2 bg-blue-600 text-white rounded-lg font-medium';
            } else if (section === 'stats') {
                document.getElementById('statsSection').classList.remove('hidden');
                document.getElementById('statsTab').className = 'px-4 py-2 bg-blue-600 text-white rounded-lg font-medium';
                initializeCharts();
            } else if (section === 'leaderboard') {
                document.getElementById('leaderboardSection').classList.remove('hidden');
                document.getElementById('leaderboardTab').className = 'px-4 py-2 bg-blue-600 text-white rounded-lg font-medium';
                updateLeaderboard();
            }
        }

        function handleRunningCalculation(e) {
            e.preventDefault();
            
            const weight = parseFloat(document.getElementById('weight').value);
            const province = document.getElementById('selectedProvince').value;
            let location = document.getElementById('locationInput').value.trim();
            const distance = parseFloat(document.getElementById('distance').value);
            const distanceUnit = document.getElementById('distanceUnit').value;
            const speed = document.getElementById('runningSpeed').value;
            const rounds = parseInt(document.getElementById('rounds').value);
            
            if (!province) {
                alert(currentLanguage === 'th' ? 'กรุณาเลือกจังหวัด' : 'Please select province');
                return;
            }
            
            if (!speed) {
                alert(currentLanguage === 'th' ? 'กรุณาเลือกระดับความเร็ว' : 'Please select speed level');
                return;
            }
            
            // If no location specified, use default
            if (!location) {
                location = 'ไม่ระบุสถานที่';
            } else {
                // Save custom location if it's new
                saveCustomLocation(province, location);
            }
            
            // Convert distance to kilometers
            let distanceInKm = distance;
            if (distanceUnit === 'm') {
                distanceInKm = distance / 1000;
            }
            
            const totalDistance = distanceInKm * rounds;
            
            // Calculate calories with speed multiplier
            const baseCalories = weight * totalDistance * 1.036; // Base running formula
            const speedMultiplier = speedMultipliers[speed];
            const calories = Math.round(baseCalories * speedMultiplier);
            
            // Save data
            const runningEntry = {
                user: currentUser,
                province: province,
                location: location,
                distance: totalDistance,
                distanceUnit: distanceUnit,
                speed: speed,
                calories: calories,
                date: new Date().toISOString(),
                week: getWeekNumber(new Date())
            };
            
            runningData.push(runningEntry);
            localStorage.setItem('runningData', JSON.stringify(runningData));
            
            // Update user's province
            users[currentUser].province = province;
            localStorage.setItem('fitTrackerUsers', JSON.stringify(users));
            
            // Show result
            const t = translations[currentLanguage];
            document.getElementById('runningResult').classList.remove('hidden');
            document.getElementById('runningCalories').textContent = `${calories} ${currentLanguage === 'th' ? 'แคลอรี่' : 'calories'}`;
            
            const distanceText = distanceUnit === 'km' ? 
                `${totalDistance} ${currentLanguage === 'th' ? 'กม.' : 'km'}` : 
                `${distance * rounds} ${currentLanguage === 'th' ? 'ม.' : 'm'}`;
            
            const locationText = location === 'ไม่ระบุสถานที่' ? 
                (currentLanguage === 'th' ? 'ไม่ระบุสถานที่' : 'Location not specified') : 
                location;
            
            document.getElementById('runningDetails').textContent = 
                `${currentLanguage === 'th' ? 'วิ่งที่' : 'Running at'} ${locationText}, ${province} ${currentLanguage === 'th' ? 'ระยะทาง' : 'distance'} ${distanceText}`;
            
            updateUserStats();
        }

        function handleGymCalculation(e) {
            e.preventDefault();
            
            const weight = parseFloat(document.getElementById('gymWeight').value);
            const exerciseType = document.getElementById('exerciseType').value;
            const reps = parseInt(document.getElementById('reps').value);
            const sets = parseInt(document.getElementById('sets').value);
            
            const totalReps = reps * sets;
            const calories = Math.round(weight * totalReps * exerciseRates[exerciseType]);
            
            // Save data
            const gymEntry = {
                user: currentUser,
                exerciseType: exerciseType,
                reps: totalReps,
                sets: sets,
                calories: calories,
                date: new Date().toISOString(),
                week: getWeekNumber(new Date())
            };
            
            gymData.push(gymEntry);
            localStorage.setItem('gymData', JSON.stringify(gymData));
            
            // Show result
            document.getElementById('gymResult').classList.remove('hidden');
            document.getElementById('gymCalories').textContent = `${calories} แคลอรี่`;
            document.getElementById('gymDetails').textContent = `${document.getElementById('exerciseType').options[document.getElementById('exerciseType').selectedIndex].text} ${totalReps} ครั้ง (${sets} เซ็ต)`;
            
            updateUserStats();
        }

        function updateUserStats() {
            const currentWeek = getWeekNumber(new Date());
            
            // Running stats
            const userRunningData = runningData.filter(entry => 
                entry.user === currentUser && entry.week === currentWeek
            );
            
            const weeklyRunningCalories = userRunningData.reduce((sum, entry) => sum + entry.calories, 0);
            const weeklyDistance = userRunningData.reduce((sum, entry) => sum + entry.distance, 0);
            
            document.getElementById('weeklyCalories').textContent = `${weeklyRunningCalories} kcal`;
            document.getElementById('weeklyDistance').textContent = `${weeklyDistance.toFixed(1)} km`;
            
            // Gym stats
            const userGymData = gymData.filter(entry => 
                entry.user === currentUser && entry.week === currentWeek
            );
            
            const weeklyGymCalories = userGymData.reduce((sum, entry) => sum + entry.calories, 0);
            const weeklySets = userGymData.reduce((sum, entry) => sum + entry.sets, 0);
            
            document.getElementById('weeklyGymCalories').textContent = `${weeklyGymCalories} kcal`;
            document.getElementById('weeklySets').textContent = `${weeklySets} sets`;
            
            // Calculate rankings
            updateRankings();
        }

        function updateRankings() {
            const currentWeek = getWeekNumber(new Date());
            const userProvince = users[currentUser]?.province;
            
            // Running rankings
            const runningStats = {};
            runningData.filter(entry => entry.week === currentWeek).forEach(entry => {
                if (!runningStats[entry.user]) {
                    runningStats[entry.user] = { calories: 0, distance: 0, province: entry.province };
                }
                runningStats[entry.user].calories += entry.calories;
                runningStats[entry.user].distance += entry.distance;
            });
            
            const sortedRunning = Object.entries(runningStats)
                .sort((a, b) => b[1].calories - a[1].calories);
            
            // National rank
            const nationalRank = sortedRunning.findIndex(([user]) => user === currentUser) + 1;
            document.getElementById('nationalRank').textContent = nationalRank > 0 ? `#${nationalRank}` : '-';
            
            // Province rank
            const provinceRunning = sortedRunning.filter(([user, data]) => data.province === userProvince);
            const provinceRank = provinceRunning.findIndex(([user]) => user === currentUser) + 1;
            document.getElementById('provinceRank').textContent = provinceRank > 0 ? `#${provinceRank}` : '-';
            
            // Gym rankings
            const gymStats = {};
            gymData.filter(entry => entry.week === currentWeek).forEach(entry => {
                if (!gymStats[entry.user]) {
                    gymStats[entry.user] = { calories: 0, sets: 0 };
                }
                gymStats[entry.user].calories += entry.calories;
                gymStats[entry.user].sets += entry.sets;
            });
            
            const sortedGym = Object.entries(gymStats)
                .sort((a, b) => b[1].calories - a[1].calories);
            
            const gymRank = sortedGym.findIndex(([user]) => user === currentUser) + 1;
            document.getElementById('gymRank').textContent = gymRank > 0 ? `#${gymRank}` : '-';
        }

        function updateLeaderboard() {
            const filter = document.getElementById('leaderboardFilter').value;
            const currentWeek = getWeekNumber(new Date());
            const userProvince = users[currentUser]?.province;
            
            // Running leaderboard
            const runningStats = {};
            runningData.filter(entry => entry.week === currentWeek).forEach(entry => {
                if (!runningStats[entry.user]) {
                    runningStats[entry.user] = { calories: 0, distance: 0, province: entry.province };
                }
                runningStats[entry.user].calories += entry.calories;
                runningStats[entry.user].distance += entry.distance;
            });
            
            let filteredRunning = Object.entries(runningStats);
            if (filter === 'province') {
                filteredRunning = filteredRunning.filter(([user, data]) => data.province === userProvince);
            }
            
            const sortedRunning = filteredRunning.sort((a, b) => b[1].calories - a[1].calories);
            
            const runningLeaderboard = document.getElementById('runningLeaderboard');
            runningLeaderboard.innerHTML = '';
            
            sortedRunning.slice(0, 10).forEach(([user, data], index) => {
                const row = document.createElement('tr');
                row.className = user === currentUser ? 'bg-blue-50' : '';
                row.innerHTML = `
                    <td class="py-2 px-2 font-semibold">${index + 1}</td>
                    <td class="py-2 px-2">${user}</td>
                    <td class="py-2 px-2">${data.calories} kcal</td>
                    <td class="py-2 px-2">${data.distance.toFixed(1)} km</td>
                `;
                runningLeaderboard.appendChild(row);
            });
            
            // Gym leaderboard
            const gymStats = {};
            gymData.filter(entry => entry.week === currentWeek).forEach(entry => {
                if (!gymStats[entry.user]) {
                    gymStats[entry.user] = { calories: 0, sets: 0 };
                }
                gymStats[entry.user].calories += entry.calories;
                gymStats[entry.user].sets += entry.sets;
            });
            
            const sortedGym = Object.entries(gymStats)
                .sort((a, b) => b[1].calories - a[1].calories);
            
            const gymLeaderboard = document.getElementById('gymLeaderboard');
            gymLeaderboard.innerHTML = '';
            
            sortedGym.slice(0, 10).forEach(([user, data], index) => {
                const row = document.createElement('tr');
                row.className = user === currentUser ? 'bg-purple-50' : '';
                row.innerHTML = `
                    <td class="py-2 px-2 font-semibold">${index + 1}</td>
                    <td class="py-2 px-2">${user}</td>
                    <td class="py-2 px-2">${data.calories} kcal</td>
                    <td class="py-2 px-2">${data.sets} sets</td>
                `;
                gymLeaderboard.appendChild(row);
            });
        }

        function getWeekNumber(date) {
            const d = new Date(Date.UTC(date.getFullYear(), date.getMonth(), date.getDate()));
            const dayNum = d.getUTCDay() || 7;
            d.setUTCDate(d.getUTCDate() + 4 - dayNum);
            const yearStart = new Date(Date.UTC(d.getUTCFullYear(),0,1));
            return Math.ceil((((d - yearStart) / 86400000) + 1)/7);
        }

        function initializeCharts() {
            if (!currentUser) return;
            
            // Destroy existing charts
            if (weeklyCaloriesChart) weeklyCaloriesChart.destroy();
            if (exerciseDistributionChart) exerciseDistributionChart.destroy();
            if (dailyProgressChart) dailyProgressChart.destroy();
            if (provinceComparisonChart) provinceComparisonChart.destroy();
            
            createWeeklyCaloriesChart();
            createExerciseDistributionChart();
            createDailyProgressChart();
            createProvinceComparisonChart();
        }

        function createWeeklyCaloriesChart() {
            const ctx = document.getElementById('weeklyCaloriesChart').getContext('2d');
            const weeks = [];
            const runningCalories = [];
            const gymCalories = [];
            
            // Get last 8 weeks of data
            const currentWeek = getWeekNumber(new Date());
            for (let i = 7; i >= 0; i--) {
                const week = currentWeek - i;
                weeks.push(`สัปดาห์ ${week}`);
                
                const weekRunning = runningData.filter(entry => 
                    entry.user === currentUser && entry.week === week
                ).reduce((sum, entry) => sum + entry.calories, 0);
                
                const weekGym = gymData.filter(entry => 
                    entry.user === currentUser && entry.week === week
                ).reduce((sum, entry) => sum + entry.calories, 0);
                
                runningCalories.push(weekRunning);
                gymCalories.push(weekGym);
            }
            
            weeklyCaloriesChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: weeks,
                    datasets: [{
                        label: 'การวิ่ง',
                        data: runningCalories,
                        borderColor: '#3B82F6',
                        backgroundColor: 'rgba(59, 130, 246, 0.1)',
                        tension: 0.4
                    }, {
                        label: 'เวท/คาร์ดิโอ',
                        data: gymCalories,
                        borderColor: '#8B5CF6',
                        backgroundColor: 'rgba(139, 92, 246, 0.1)',
                        tension: 0.4
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'top',
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'แคลอรี่ (kcal)'
                            }
                        }
                    }
                }
            });
        }

        function createExerciseDistributionChart() {
            const ctx = document.getElementById('exerciseDistributionChart').getContext('2d');
            const currentWeek = getWeekNumber(new Date());
            
            // Calculate running vs gym calories
            const runningTotal = runningData.filter(entry => 
                entry.user === currentUser && entry.week === currentWeek
            ).reduce((sum, entry) => sum + entry.calories, 0);
            
            const gymTotal = gymData.filter(entry => 
                entry.user === currentUser && entry.week === currentWeek
            ).reduce((sum, entry) => sum + entry.calories, 0);
            
            exerciseDistributionChart = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: ['การวิ่ง', 'เวท/คาร์ดิโอ'],
                    datasets: [{
                        data: [runningTotal, gymTotal],
                        backgroundColor: ['#3B82F6', '#8B5CF6'],
                        borderWidth: 2,
                        borderColor: '#ffffff'
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'bottom',
                        }
                    }
                }
            });
        }

        function createDailyProgressChart() {
            const ctx = document.getElementById('dailyProgressChart').getContext('2d');
            const days = [];
            const dailyCalories = [];
            
            // Get last 7 days
            for (let i = 6; i >= 0; i--) {
                const date = new Date();
                date.setDate(date.getDate() - i);
                const dayName = date.toLocaleDateString('th-TH', { weekday: 'short' });
                days.push(dayName);
                
                const dayCalories = [...runningData, ...gymData].filter(entry => {
                    const entryDate = new Date(entry.date);
                    return entry.user === currentUser && 
                           entryDate.toDateString() === date.toDateString();
                }).reduce((sum, entry) => sum + entry.calories, 0);
                
                dailyCalories.push(dayCalories);
            }
            
            dailyProgressChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: days,
                    datasets: [{
                        label: 'แคลอรี่รวม',
                        data: dailyCalories,
                        backgroundColor: 'rgba(34, 197, 94, 0.8)',
                        borderColor: '#22C55E',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: false
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'แคลอรี่ (kcal)'
                            }
                        }
                    }
                }
            });
        }

        function createProvinceComparisonChart() {
            const ctx = document.getElementById('provinceComparisonChart').getContext('2d');
            const currentWeek = getWeekNumber(new Date());
            
            // Calculate calories by province
            const provinceStats = {};
            [...runningData, ...gymData].filter(entry => entry.week === currentWeek).forEach(entry => {
                const province = entry.province || users[entry.user]?.province || 'ไม่ระบุ';
                if (!provinceStats[province]) {
                    provinceStats[province] = 0;
                }
                provinceStats[province] += entry.calories;
            });
            
            const provinces = Object.keys(provinceStats).slice(0, 10);
            const calories = provinces.map(province => provinceStats[province]);
            
            provinceComparisonChart = new Chart(ctx, {
                type: 'horizontalBar',
                data: {
                    labels: provinces,
                    datasets: [{
                        label: 'แคลอรี่รวม',
                        data: calories,
                        backgroundColor: 'rgba(249, 115, 22, 0.8)',
                        borderColor: '#F97316',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: false
                        }
                    },
                    scales: {
                        x: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'แคลอรี่ (kcal)'
                            }
                        }
                    }
                }
            });
        }

        function addSampleData() {
            const sampleUsers = ['นักวิ่งมือโปร', 'ฟิตเนสคิง', 'รันเนอร์หญิง', 'เวทเทรนเนอร์', 'คาร์ดิโอควีน'];
            const currentWeek = getWeekNumber(new Date());
            
            sampleUsers.forEach((user, index) => {
                users[user] = { password: '123456', province: Object.keys(provinceData)[index % 10] };
                
                // Add running data for multiple weeks
                for (let week = 0; week < 8; week++) {
                    for (let i = 0; i < Math.random() * 3 + 1; i++) {
                        const date = new Date();
                        date.setDate(date.getDate() - (week * 7) - Math.random() * 7);
                        
                        runningData.push({
                            user: user,
                            province: users[user].province,
                            location: provinceData[users[user].province][0],
                            distance: 3 + Math.random() * 7,
                            calories: 200 + Math.random() * 400,
                            date: date.toISOString(),
                            week: currentWeek - week
                        });
                    }
                }
                
                // Add gym data for multiple weeks
                for (let week = 0; week < 8; week++) {
                    for (let i = 0; i < Math.random() * 2 + 1; i++) {
                        const date = new Date();
                        date.setDate(date.getDate() - (week * 7) - Math.random() * 7);
                        
                        gymData.push({
                            user: user,
                            exerciseType: ['pushup', 'situp', 'squat', 'pullup'][Math.floor(Math.random() * 4)],
                            reps: 50 + Math.random() * 100,
                            sets: 3 + Math.random() * 2,
                            calories: 100 + Math.random() * 200,
                            date: date.toISOString(),
                            week: currentWeek - week
                        });
                    }
                }
            });
            
            localStorage.setItem('fitTrackerUsers', JSON.stringify(users));
            localStorage.setItem('runningData', JSON.stringify(runningData));
            localStorage.setItem('gymData', JSON.stringify(gymData));
        }
    </script>
<script>(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'98aeabd15460731f',t:'MTc1OTg1MzQ1My4wMDAwMDA='};var a=document.createElement('script');a.nonce='';a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script></body>
</html>
