PGDMP  .    .                |            insurgent_db    16.2    16.2 2                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            !           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            "           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            #           1262    33153    insurgent_db    DATABASE     �   CREATE DATABASE insurgent_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE insurgent_db;
                postgres    false            �            1255    41634    add_sched()    FUNCTION       CREATE FUNCTION public.add_sched() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
begin
	if new.status = 'Regular' or new.status = 'Reserve' then
	insert into shift(s_id,schedule_id,seconds,status)
				values(default,new.schedule_id,0,0);
	end if;
return new;
end;
$$;
 "   DROP FUNCTION public.add_sched();
       public          postgres    false            �            1259    33438    departments    TABLE     r   CREATE TABLE public.departments (
    department_id integer NOT NULL,
    name character varying(100) NOT NULL
);
    DROP TABLE public.departments;
       public         heap    postgres    false            �            1259    33437    departments_department_id_seq    SEQUENCE     �   CREATE SEQUENCE public.departments_department_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.departments_department_id_seq;
       public          postgres    false    217            $           0    0    departments_department_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.departments_department_id_seq OWNED BY public.departments.department_id;
          public          postgres    false    216            �            1259    33447 	   employees    TABLE     k  CREATE TABLE public.employees (
    employee_id integer NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(50) NOT NULL,
    email character varying(100) NOT NULL,
    phone character varying(15),
    address character varying(255),
    hire_date date NOT NULL,
    department_id integer,
    emp_pin character varying(4)
);
    DROP TABLE public.employees;
       public         heap    postgres    false            �            1259    33446    employees_employee_id_seq    SEQUENCE     �   CREATE SEQUENCE public.employees_employee_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.employees_employee_id_seq;
       public          postgres    false    219            %           0    0    employees_employee_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.employees_employee_id_seq OWNED BY public.employees.employee_id;
          public          postgres    false    218            �            1259    33475    payroll    TABLE       CREATE TABLE public.payroll (
    payroll_id integer NOT NULL,
    employee_id integer,
    pay_date date NOT NULL,
    hours_worked numeric(5,2) NOT NULL,
    pay_rate numeric(10,2) NOT NULL,
    gross_pay numeric(10,2) NOT NULL,
    net_pay numeric(10,2) NOT NULL
);
    DROP TABLE public.payroll;
       public         heap    postgres    false            �            1259    33474    payroll_payroll_id_seq    SEQUENCE     �   CREATE SEQUENCE public.payroll_payroll_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.payroll_payroll_id_seq;
       public          postgres    false    223            &           0    0    payroll_payroll_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.payroll_payroll_id_seq OWNED BY public.payroll.payroll_id;
          public          postgres    false    222            �            1259    33461 	   schedules    TABLE     �   CREATE TABLE public.schedules (
    schedule_id integer NOT NULL,
    employee_id integer,
    shift_date date NOT NULL,
    status character varying(20) DEFAULT 'Scheduled'::character varying,
    start_time integer,
    end_time integer
);
    DROP TABLE public.schedules;
       public         heap    postgres    false            �            1259    33460    schedules_schedule_id_seq    SEQUENCE     �   CREATE SEQUENCE public.schedules_schedule_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.schedules_schedule_id_seq;
       public          postgres    false    221            '           0    0    schedules_schedule_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.schedules_schedule_id_seq OWNED BY public.schedules.schedule_id;
          public          postgres    false    220            �            1259    41621    shift    TABLE     �   CREATE TABLE public.shift (
    s_id integer NOT NULL,
    schedule_id integer,
    seconds integer,
    status integer NOT NULL
);
    DROP TABLE public.shift;
       public         heap    postgres    false            �            1259    41620    shift_s_id_seq    SEQUENCE     �   CREATE SEQUENCE public.shift_s_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.shift_s_id_seq;
       public          postgres    false    225            (           0    0    shift_s_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.shift_s_id_seq OWNED BY public.shift.s_id;
          public          postgres    false    224            �            1259    33154    users    TABLE     x   CREATE TABLE public.users (
    username character varying(20) NOT NULL,
    password character varying(20) NOT NULL
);
    DROP TABLE public.users;
       public         heap    postgres    false            i           2604    33441    departments department_id    DEFAULT     �   ALTER TABLE ONLY public.departments ALTER COLUMN department_id SET DEFAULT nextval('public.departments_department_id_seq'::regclass);
 H   ALTER TABLE public.departments ALTER COLUMN department_id DROP DEFAULT;
       public          postgres    false    217    216    217            j           2604    33450    employees employee_id    DEFAULT     ~   ALTER TABLE ONLY public.employees ALTER COLUMN employee_id SET DEFAULT nextval('public.employees_employee_id_seq'::regclass);
 D   ALTER TABLE public.employees ALTER COLUMN employee_id DROP DEFAULT;
       public          postgres    false    218    219    219            m           2604    33478    payroll payroll_id    DEFAULT     x   ALTER TABLE ONLY public.payroll ALTER COLUMN payroll_id SET DEFAULT nextval('public.payroll_payroll_id_seq'::regclass);
 A   ALTER TABLE public.payroll ALTER COLUMN payroll_id DROP DEFAULT;
       public          postgres    false    222    223    223            k           2604    33464    schedules schedule_id    DEFAULT     ~   ALTER TABLE ONLY public.schedules ALTER COLUMN schedule_id SET DEFAULT nextval('public.schedules_schedule_id_seq'::regclass);
 D   ALTER TABLE public.schedules ALTER COLUMN schedule_id DROP DEFAULT;
       public          postgres    false    221    220    221            n           2604    41624 
   shift s_id    DEFAULT     h   ALTER TABLE ONLY public.shift ALTER COLUMN s_id SET DEFAULT nextval('public.shift_s_id_seq'::regclass);
 9   ALTER TABLE public.shift ALTER COLUMN s_id DROP DEFAULT;
       public          postgres    false    224    225    225                      0    33438    departments 
   TABLE DATA           :   COPY public.departments (department_id, name) FROM stdin;
    public          postgres    false    217   [;                 0    33447 	   employees 
   TABLE DATA           �   COPY public.employees (employee_id, first_name, last_name, email, phone, address, hire_date, department_id, emp_pin) FROM stdin;
    public          postgres    false    219   �;                 0    33475    payroll 
   TABLE DATA           p   COPY public.payroll (payroll_id, employee_id, pay_date, hours_worked, pay_rate, gross_pay, net_pay) FROM stdin;
    public          postgres    false    223   q=                 0    33461 	   schedules 
   TABLE DATA           g   COPY public.schedules (schedule_id, employee_id, shift_date, status, start_time, end_time) FROM stdin;
    public          postgres    false    221   �=                 0    41621    shift 
   TABLE DATA           C   COPY public.shift (s_id, schedule_id, seconds, status) FROM stdin;
    public          postgres    false    225   �=                 0    33154    users 
   TABLE DATA           3   COPY public.users (username, password) FROM stdin;
    public          postgres    false    215   �=       )           0    0    departments_department_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.departments_department_id_seq', 1, false);
          public          postgres    false    216            *           0    0    employees_employee_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.employees_employee_id_seq', 28, true);
          public          postgres    false    218            +           0    0    payroll_payroll_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.payroll_payroll_id_seq', 1, false);
          public          postgres    false    222            ,           0    0    schedules_schedule_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.schedules_schedule_id_seq', 33, true);
          public          postgres    false    220            -           0    0    shift_s_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.shift_s_id_seq', 20, true);
          public          postgres    false    224            r           2606    33445     departments departments_name_key 
   CONSTRAINT     [   ALTER TABLE ONLY public.departments
    ADD CONSTRAINT departments_name_key UNIQUE (name);
 J   ALTER TABLE ONLY public.departments DROP CONSTRAINT departments_name_key;
       public            postgres    false    217            t           2606    33443    departments departments_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.departments
    ADD CONSTRAINT departments_pkey PRIMARY KEY (department_id);
 F   ALTER TABLE ONLY public.departments DROP CONSTRAINT departments_pkey;
       public            postgres    false    217            v           2606    33454    employees employees_email_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_email_key UNIQUE (email);
 G   ALTER TABLE ONLY public.employees DROP CONSTRAINT employees_email_key;
       public            postgres    false    219            x           2606    33452    employees employees_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_pkey PRIMARY KEY (employee_id);
 B   ALTER TABLE ONLY public.employees DROP CONSTRAINT employees_pkey;
       public            postgres    false    219            |           2606    33480    payroll payroll_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.payroll
    ADD CONSTRAINT payroll_pkey PRIMARY KEY (payroll_id);
 >   ALTER TABLE ONLY public.payroll DROP CONSTRAINT payroll_pkey;
       public            postgres    false    223            z           2606    33468    schedules schedules_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.schedules
    ADD CONSTRAINT schedules_pkey PRIMARY KEY (schedule_id);
 B   ALTER TABLE ONLY public.schedules DROP CONSTRAINT schedules_pkey;
       public            postgres    false    221            ~           2606    41626    shift shift_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.shift
    ADD CONSTRAINT shift_pkey PRIMARY KEY (s_id);
 :   ALTER TABLE ONLY public.shift DROP CONSTRAINT shift_pkey;
       public            postgres    false    225            p           2606    33158    users users_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (username);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    215            �           2620    41635    schedules schedule_add    TRIGGER     o   CREATE TRIGGER schedule_add AFTER INSERT ON public.schedules FOR EACH ROW EXECUTE FUNCTION public.add_sched();
 /   DROP TRIGGER schedule_add ON public.schedules;
       public          postgres    false    221    226                       2606    33455 &   employees employees_department_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_department_id_fkey FOREIGN KEY (department_id) REFERENCES public.departments(department_id);
 P   ALTER TABLE ONLY public.employees DROP CONSTRAINT employees_department_id_fkey;
       public          postgres    false    219    4724    217            �           2606    33481     payroll payroll_employee_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.payroll
    ADD CONSTRAINT payroll_employee_id_fkey FOREIGN KEY (employee_id) REFERENCES public.employees(employee_id);
 J   ALTER TABLE ONLY public.payroll DROP CONSTRAINT payroll_employee_id_fkey;
       public          postgres    false    219    223    4728            �           2606    33469 $   schedules schedules_employee_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.schedules
    ADD CONSTRAINT schedules_employee_id_fkey FOREIGN KEY (employee_id) REFERENCES public.employees(employee_id);
 N   ALTER TABLE ONLY public.schedules DROP CONSTRAINT schedules_employee_id_fkey;
       public          postgres    false    4728    219    221            �           2606    41627    shift shift_schedule_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.shift
    ADD CONSTRAINT shift_schedule_id_fkey FOREIGN KEY (schedule_id) REFERENCES public.schedules(schedule_id) ON UPDATE CASCADE ON DELETE CASCADE;
 F   ALTER TABLE ONLY public.shift DROP CONSTRAINT shift_schedule_id_fkey;
       public          postgres    false    4730    225    221               L   x�340��(�M�SJ-�/-JN-�240��J��,�/��9�SsrRALΐ�t����L ϔ�71/1(���� 8:         �  x����n�0�����<��F�H�U=$�^���aM�fԧ��l�&��J�m���7���4Op�^�C��>�������a>�iZn;�Q*���G��~)��BRPP��up�)�����M!��~���ƩE'�խlP��R�`BqD.m�u�P�fI�.�T)#2��V�O>g.��� D�G����� ��9|��5����*-����Uh�H��Qy�r�����ϱO�|�ҚF6�J�>}C�P���'�T��u�]U]���/�ȵixK���5��.�1�4S�i��a�2�O�a;��*mx�Z�QO�a]��=]��;Vd�k�`��]�a�T�g����|t.�UO��v��Q�Bu2x)%�ӛ:��}����s���P���}�r�����.7ִ5��N�����ٷ�1��s�	            x������ � �         2   x�36�4�4202�50�5��JM/�I,�44�4�26��!i����� ��	            x�3��46�4�4�22�46�b���� -qJ         /   x�KL����L�\%��%� �+=?��� ��H;YYp��qqq l�4     